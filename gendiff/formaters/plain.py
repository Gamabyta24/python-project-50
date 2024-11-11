def format_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value).lower()


def format_plain(diff):
    lines = []

    def walk(diff, path=""):
        status_handlers = {
            "added": added(),
            "deleted": removed(),
            "modified": updated(),
            "nested": nested(walk),
        }

        for item in diff:
            key = item["name"]
            status = item["action"]
            property_path = f"{path}.{key}".strip(".")

            handler = status_handlers.get(status)
            if handler:
                result = handler(item, property_path)
                if result:
                    lines.append(result)

    walk(diff)
    return "\n".join(lines)


def added():
    return (
        lambda item, path:
        f"Property '{path}' was added with value: {format_value(item['new_value'])}"
    )


def removed():
    return lambda item, path: f"Property '{path}' was removed"


def updated():
    return lambda item, path: (
        f"Property '{path}' was updated. From {format_value(item['old_value'])} "
        f"to {format_value(item['new_value'])}"
    )


def nested(walk):
    return lambda item, path: walk(item["children"], path)
