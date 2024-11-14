import json


def pretty_print(data, title=None):
    try:
        data_preview = json.dumps(data, indent=4)
    except TypeError:
        data_preview = json.dumps(f"{data}", indent=4)
    print(f"{title}:\n{data_preview}" if title else data_preview)
