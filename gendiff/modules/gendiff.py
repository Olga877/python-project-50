from gendiff.formatters.stylish_formatter import format_data_stylish
from gendiff.formatters.plain_formatter import format_data_plain



# def sort_keys_with_symbols(d):
#     sorted_dict = {}
#     for key in sorted(d.keys(), key=lambda x: x.lstrip(' +-')):
#         value = d[key]
#         if isinstance(value, dict):
#             sorted_dict[key] = sort_keys_with_symbols(value)
#         else:
#             sorted_dict[key] = value
#     return sorted_dict


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
                    diff[k] = {'type': 'updated', "old_value": a[k], "new_value": b[k]}
            else:
                diff[k] = {"type": "removed", "value": a[k]}
        for k in b.keys():
            if k not in a:
                diff[k] = {"type": "added", "value": b[k]}
        return diff

    if formatter == 'stylish':
        return format_data_stylish(compare(d1, d2), " ", 4)
    elif formatter == 'plain':
        return format_data_plain(compare(d1, d2))
    else:
        raise ValueError("Unsupported format")
    
    


