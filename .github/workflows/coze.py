import itertools
import os
from dataclasses import dataclass
from cozepy import Coze, TokenAuth, JWTOAuthApp, DocumentBase, DocumentSourceInfo, DocumentUpdateRule, Document


@dataclass
class AuthData:
    """
    DTO for storing data related to authorization/authentication process to access Coze services remotely via API
    """

    app_id: str
    private_key: str
    public_key: str

    @staticmethod
    def from_data(app_id: str, private_key: str, public_key: str):
        """
        Creating AuthData DTO from explicitly specified data, passed as parameters
        :param app_id: OAuth App ID (previously created in Coze at browser side)
        :param private_key: raw text content of the private key file (.pem), downloaded from OAuth App webpage
        :param public_key: content of the public key string, displayed on OAuth App webpage
        :return: AuthData object, created from provided data
        """
        return AuthData(app_id, private_key, public_key)

    @staticmethod
    def from_environment(app_id="COZE_OAUTH_APP_ID", private_key="COZE_PRIVATE_KEY", public_key="COZE_PUBLIC_KEY"):
        """
        Creating AuthData DTO from data stored as environmental variables
        :param app_id: name of the variable that stores OAuth App ID
            (defaults to "COZE_OAUTH_APP_ID")
        :param private_key: name of the variable that stores content of the private key file (.pem)
            (defaults to "COZE_PRIVATE_KEY")
        :param public_key: name of the variable that stores content of the public key string
            (defaults to "COZE_PUBLIC_KEY")
        :return: AuthData object, created from provided environmental variables
        """
        return AuthData(os.environ[app_id], os.environ[private_key], os.environ[public_key])


@dataclass
class KnowledgeData:
    """
    DTO for storing data required to access some of API endpoints related to Coze Knowledge remote documents
    """

    knowledge_id: str

    @staticmethod
    def from_data(knowledge_id: str):
        """
        Creating KnowledgeData DTO from explicitly specified data, passed as parameters
        :param knowledge_id: ID of the target knowledge (can be found directly in the browser URL field)
        :return: KnowledgeData object, created from provided data
        """
        return KnowledgeData(knowledge_id=knowledge_id)

    @staticmethod
    def from_environment(knowledge_id_var: str = "COZE_KNOWLEDGE_ID"):
        """
        Creating KnowledgeData DTO from data stored as environmental variables
        :param knowledge_id_var: name of the variable that stores ID of the target knowledge
            (defaults to "COZE_KNOWLEDGE_ID")
        :return: KnowledgeData object, created from provided environmental variables
        """
        return KnowledgeData(knowledge_id=os.environ[knowledge_id_var])


class CozeKnowledgeWrapper:
    """
    Custom wrapper class to simplify interaction with Coze Knowledge API endpoints using coze-py package
    """

    # Limitation of how many documents can be created within one request (specified by Coze in their API docs page)
    CREATE_OBJECTS_LIMIT_PER_REQUEST = 10

    # Limitation of how many documents can be deleted within one request (specified by Coze in their API docs page)
    DELETE_OBJECTS_LIMIT_PER_REQUEST = 100

    def __init__(self, knowledge_data: KnowledgeData, auth_data: AuthData):
        """
        Main constructor, requires both knowledge data and auth data, provided as objects of custom DTO classes,
        defined above
        :param knowledge_data: KnowledgeData DTO, used to clarify which remote knowledge to work with
        :param auth_data: AuthData DTO, used to get access to Coze API before starting to interact with any knowledge
        """

        # Creating core instance to interact with, in order to access Coze API
        self.__authorize(auth_data)
        self.coze_instance = Coze(auth=TokenAuth(self.access_token))

        # Creating redirect links from internal methods to coze-py package methods (some kind of virtual bridge)
        __documents = self.coze_instance.knowledge.documents
        self.__create = __documents.create
        self.__list = __documents.list
        self.__update = __documents.update
        self.__delete = __documents.delete

        # Saving target knowledge ID as class field to access it later for some API endpoints
        self.knowledge_id = knowledge_data.knowledge_id

    def create_documents(self, urls: list[str], update_interval_in_hours=24 * 7) -> list[Document]:
        """
        Request to create new remote documents in currently specified Knowledge
        :param urls: list of URLs used as content sources for each document
        :param update_interval_in_hours: source URL content synchronization frequency, specified in hours
            (defaults to 24 * 7, in other words, 7 days or 1 week)
        :return: list of all successfully created new documents, returned in response from the remote side
        """

        # Preparing each document to make object structure required by Coze API
        document_bases: list[DocumentBase] = []
        for url in urls:
            src_info = DocumentSourceInfo.build_web_page(url=url)
            auto_update = DocumentUpdateRule.build_auto_update(interval=update_interval_in_hours)
            document_base = DocumentBase(name=url, source_info=src_info, update_rule=auto_update)
            document_bases.append(document_base)

        # Splitting the list of prepared documents to equally sized groups (chunks/batches)
        # (this is required because Coze API has such limitations on documents amount per single request)
        objects_limit = self.CREATE_OBJECTS_LIMIT_PER_REQUEST
        document_bases_batched = itertools.batched(document_bases, objects_limit)

        # Creating all prepared documents remotely group by group in order, then returning the result back
        created_documents: list[Document] = []
        for batch in document_bases_batched:
            created_batch = self.__create(dataset_id=self.knowledge_id, document_bases=list(batch))
            created_documents += created_batch

        return created_documents

    def list_documents(self) -> list[Document]:
        """
        Request to get a list of all currently existing documents on remote Knowledge side
        :return: list of all documents found remotely for currently specified Knowledge
        """

        # Starting from the empty list, then going to fetch all documents in multiple steps
        # (this is needed because this API endpoint splits results to pages, so, checking all pages one by one)
        found_documents: list[Document] = []

        # Checking existing remote documents from the default first page, and adding them to the local list
        documents_page = self.__list(dataset_id=self.knowledge_id)
        found_documents += documents_page.items

        # If there are still any documents left at other pages, checking them too until reaching the end of remote list
        while documents_page.has_more:
            # Adding all these documents to the local list as well
            documents_page = self.__list(dataset_id=self.knowledge_id, page_num=documents_page.page_num + 1)
            found_documents += documents_page.items

        return found_documents

    def update_document(self, document_id: str, document_name: str, update_interval_in_hours: int) -> None:
        """
        Request to update existing document on remote Knowledge side
        :param document_id: ID of the document to be updated
        :param document_name: new name for this document
        :param update_interval_in_hours: new synchronization frequency for this document, specified in hours
        :return:
        """

        # Preparing provided data to make proper structure required for this API endpoint, then sending update request
        auto_update = DocumentUpdateRule.build_auto_update(interval=update_interval_in_hours)
        self.__update(document_id=document_id, document_name=document_name, update_rule=auto_update)

    def delete_documents(self, document_ids: list[str]) -> None:
        """
        Request to delete existing documents on remote Knowledge side
        :param document_ids: list of IDs for each document to be deleted
        :return:
        """

        # Splitting the list of prepared document IDs to equally sized groups (chunks/batches)
        # (this is required because Coze API has such limitations on documents amount per single request)
        objects_limit = self.DELETE_OBJECTS_LIMIT_PER_REQUEST
        ids_batched = itertools.batched(document_ids, objects_limit)

        # Deleting all requested documents remotely group by group in order
        for batch in ids_batched:
            self.__delete(document_ids=list(batch))

    def __authorize(self, auth_data: AuthData) -> None:
        """
        Internal method used to get new access token using JWT OAuth logic
        :param auth_data: AuthData DTO that contains all data needed for JWT OAuth to succeed
        :return:
        """

        # Creating JWT OAuth App class object, providing all required auth data, and requesting the access token
        jwt_oauth_app = JWTOAuthApp(
            client_id=auth_data.app_id,
            private_key=auth_data.private_key,
            public_key_id=auth_data.public_key
        )
        self.access_token = jwt_oauth_app.get_access_token().access_token
