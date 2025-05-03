from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain_formatter import format_plain
from gendiff.formatters.stylish_formatter import format_stylish


def generate_diff(d1, d2, formatter='stylish'):
    def compare(a, b):
        diff = {}
        for k in a.keys():
            if k in b:
                if isinstance(a[k], dict) and isinstance(b[k], dict):
                    nested_diff = compare(a[k], b[k])
                    if nested_diff:
                        diff[k] = nested_diff
                elif a[k] == b[k]:
                    diff[k] = a[k]
                else:
                    diff[k] = {'type': 'updated', "old_value": a[k],
                               "new_value": b[k]}
            else:
                diff[k] = {"type": "removed", "value": a[k]}
        for k in b.keys():
            if k not in a:
                diff[k] = {"type": "added", "value": b[k]}
        return diff

    if formatter == 'stylish':
        return format_stylish(compare(d1, d2), " ", 4)
    elif formatter == 'plain':
        return format_plain(compare(d1, d2))
    elif formatter == 'json':
        return format_json(compare(d1, d2))
    else:
        raise ValueError("Unsupported format")
    
    


