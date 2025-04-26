import itertools


def format_data(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent_with_symbol_size = depth + spaces_count - 2
        deep_indent_with_symbol = replacer * deep_indent_with_symbol_size
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if key[0] == "-" or key[0] == "+":
                lines.append(f'{deep_indent_with_symbol}{key}: {iter_(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        final = itertools.chain("{", lines, [current_indent + "}"])
        result = '\n'.join(final)
        return format_text(result)

    return iter_(value, 0)



def format_text(text):
    replacements = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text