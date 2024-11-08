def format_plain(diff):
    lines = []

    def format_value(value):
        if isinstance(value, dict) or isinstance(value, list):
            return '[complex value]'
        elif isinstance(value, str):
            return f"'{value}'"
        return str(value).lower() 

    def walk(diff, path=''):
        for item in diff:
            key = item['key']
            status = item['status']
            property_path = f"{path}.{key}".strip('.')

            if status == 'added':
                lines.append(
                    f"Property '{property_path}' was added with value: {format_value(item['value'])}"
                )
            elif status == 'removed':
                lines.append(f"Property '{property_path}' was removed")
            elif status == 'updated':
                lines.append(
                    f"Property '{property_path}' was updated. From {format_value(item['old_value'])} "
                    f"to {format_value(item['new_value'])}"
                )
            elif status == 'nested':
                walk(item['children'], property_path)

    walk(diff)
    return '\n'.join(lines)
