def format_stylish(diff, depth=0):
    indent = "    " * depth
    lines = ["{"]

    for item in diff:
        key = item["key"]
        status = item["status"]
        lines.append(format_item(item, status, key, depth))

    lines.append(indent + "}")
    return "\n".join(lines)


def format_item(item, status, key, depth):
    indent = "    " * depth
    if status == "nested":
        children = format_stylish(item["children"], depth + 1)
        return f"{indent}    {key}: {children}"
    elif status == "added":
        return f"{indent}  + {key}: {item['value']}"
    elif status == "removed":
        return f"{indent}  - {key}: {item['value']}"
    elif status == "updated":
        old_value = f"{indent}  - {key}: {item['old_value']}"
        new_value = f"{indent}  + {key}: {item['new_value']}"
        return f"{old_value}\n{new_value}"
    elif status == "unchanged":
        return f"{indent}    {key}: {item['value']}"
