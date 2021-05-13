"""Main module."""
import json


def read_jsonl_lazily(path):
    with open(path) as f:
        for line in f:
            yield json.loads(line)


def inspect(structure, data):
    for key, value in data.items():
        if key not in structure.keys():
            value_type = type(value)
            # Base case : Is not a dict
            if value_type is not dict:
                structure[key] = str(value_type)
            else:
                structure[key] = inspect({}, value)
    return structure


def inspect_jsonl(path):
    structure = {}
    for line_data in read_jsonl_lazily(path):
        structure = inspect(structure, line_data)
    return structure


if __name__ == "__main__":
    print(inspect_jsonl("tests/nested.jsonl"))
