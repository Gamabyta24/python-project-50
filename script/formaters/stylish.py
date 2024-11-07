def format_stylish(diff, depth=0):
    indent = '    ' * depth
    lines = ['{']

    for item in diff:
        key = item['key']
        status = item['status']
        
        if status == 'nested':
            children = format_stylish(item['children'], depth + 1)
            lines.append(f"{indent}    {key}: {children}")
        elif status == 'added':
            lines.append(f"{indent}  + {key}: {item['value']}")
        elif status == 'removed':
            lines.append(f"{indent}  - {key}: {item['value']}")
        elif status == 'updated':
            lines.append(f"{indent}  - {key}: {item['old_value']}")
            lines.append(f"{indent}  + {key}: {item['new_value']}")
        elif status == 'unchanged':
            lines.append(f"{indent}    {key}: {item['value']}")

    lines.append(indent + '}')
    return '\n'.join(lines)
