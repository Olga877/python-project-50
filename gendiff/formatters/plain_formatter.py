def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    else:
        return str(value).lower()


def format_plain(diff):
    lines = []

    def iter_(node, parent=''):
        for key, val in sorted(node.items()):
            property_path = f'{parent}.{key}' if parent else key
            if isinstance(val, dict):
                if val.get('type') == 'removed':
                    lines.append(f"Property '{property_path}' was removed")
                elif val.get('type') == 'updated':
                    old_value = format_value(val['old_value'])
                    new_value = format_value(val['new_value'])
                    lines.append(f"Property '{property_path}' was updated. "
                                 f"From {old_value} to {new_value}")
                elif val.get('type') == 'added':
                    lines.append(f"Property '{property_path}' "
                                 f"was added with value: "
                                 f"{format_value(val['value'])}")
                else:
                    iter_(val, property_path)
    iter_(diff)
    return '\n'.join(lines)