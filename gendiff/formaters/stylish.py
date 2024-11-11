SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '

def to_str(value, depth=2):
    """Рекурсивная функция для преобразования значений в строковый формат с учётом отступов."""
    indent = SEPARATOR * depth
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = [f"{indent}{{"]
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {to_str(val, depth + 4)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    return str(value)


def format_stylish(diff, depth=2):
    """Основная функция для форматирования diff в нужный стиль."""
    lines = []
    for item in diff:
        key = item["key"]
        status = item["status"]
        indent = SEPARATOR * depth

        if status == "unchanged":
            lines.append(f"{indent}  {key}: {to_str(item['value'], depth)}")
        elif status == "added":
            lines.append(f"{indent}{ADD}{key}: {to_str(item['value'], depth)}")
        elif status == "removed":
            lines.append(f"{indent}{DELETE}{key}: {to_str(item['value'], depth)}")
        elif status == "updated":
            lines.append(f"{indent}{DELETE}{key}: {to_str(item['old_value'], depth)}")
            lines.append(f"{indent}{ADD}{key}: {to_str(item['new_value'], depth)}")
        elif status == "nested":
            lines.append(f"{indent}  {key}: {format_stylish(item['children'], depth + 4)}")

    return "{\n" + "\n".join(lines) + f"\n{SEPARATOR * (depth - 2)}}}"
