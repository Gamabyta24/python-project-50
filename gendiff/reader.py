import yaml
import json
import os


def read_file(file_path):
    """Read file from folder"""
    extension = os.path.splitext(file_path)[1].lower()
    with open(file_path, "r") as file:
        if extension == ".json":
            return json.load(file)
        elif extension in {".yaml", ".yml"}:
            return yaml.safe_load(file)
        raise ValueError(f"Unknown format: {extension}")
