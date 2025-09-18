import json
import os

def read_json(file_name):

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


    file_path = os.path.join(project_root, "main", "resources", file_name)


    print(f"Reading JSON from: {file_path}")

    with open(file_path, "r") as f:
        data = json.load(f)

    return data