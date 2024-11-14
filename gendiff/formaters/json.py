import json


def format_json(diff):
    """transforms differents from list to str in 'json' format."""
    return json.dumps(diff, indent=2)
