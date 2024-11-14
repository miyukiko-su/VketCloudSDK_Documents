import os
from coze import CozeKnowledgeWrapper, AuthData, KnowledgeData
from utils import pretty_print


def make_url_from_filepath(filepath):
    repo = os.environ["REPOSITORY_NAME"]
    branch = os.environ["BRANCH_NAME"]

    relpath = os.path.relpath(filepath, os.getcwd())
    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{relpath}"

    return url


def get_local_urls():
    local_files = [os.path.join(root, filename) for root, _, files in os.walk(os.getcwd()) for filename in files]
    local_md_files = [file for file in local_files if file.casefold().endswith(".md")]
    md_file_urls = [make_url_from_filepath(filepath) for filepath in local_md_files]

    return md_file_urls


def get_remote_docs(knowledge):
    return knowledge.list_documents()


def add_new_urls(urls_to_add, knowledge):
    if not urls_to_add:
        print("There are no new files to add to knowledge. Skipping...")
        return

    knowledge.create_documents(urls_to_add)


def delete_old_urls(urls_to_delete, knowledge):
    if not urls_to_delete:
        print("There are no obsolete files to delete from knowledge. Skipping...")
        return

    document_ids = [doc.document_id for doc in get_remote_docs(knowledge) if doc.name in urls_to_delete]
    knowledge.delete_documents(document_ids)


def main():
    auth_data = AuthData.from_environment()
    knowledge_data = KnowledgeData.from_environment()
    knowledge = CozeKnowledgeWrapper(knowledge_data, auth_data)

    remote_urls = {doc.name for doc in get_remote_docs(knowledge)}
    pretty_print(remote_urls, title="Currently uploaded Coze documents")

    local_urls = set(get_local_urls())
    pretty_print(local_urls, title="Locally available markdown files")

    if remote_urls == local_urls:
        print("Documents are already up-to-date. Finished without updating anything.")
        return

    urls_to_add = list(local_urls - remote_urls)
    pretty_print(urls_to_add, title="Creating new documents")
    add_new_urls(urls_to_add, knowledge)

    # having bugs from the Coze side now, wrapping this part in try-except block just in case
    try:
        urls_to_delete = list(remote_urls - local_urls)
        pretty_print(urls_to_delete, title="Deleting documents (obsolete ones)")
        delete_old_urls(urls_to_delete, knowledge)
    except Exception as e:
        pretty_print(e)

    current_remote_docs = get_remote_docs(knowledge)
    pretty_print(current_remote_docs, title="Remote Coze documents list after this update")


if __name__ == "__main__":
    main()
