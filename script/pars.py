import yaml
import json
import os
def read_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    print(extension)
    with open(file_path, "r") as file:
        if extension == '.json':
            return json.load(file)
        elif extension in {'.yaml', '.yml'}:
            return yaml.safe_load(file)
        return json.load(file)