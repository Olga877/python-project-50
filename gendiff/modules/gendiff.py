from gendiff.modules.stylish_formatter import format_data


def sort_keys_with_symbols(d):
    sorted_dict = {}
    for key in sorted(d.keys(), key=lambda x: x.lstrip(' +-')):
        value = d[key]
        if isinstance(value, dict):
            sorted_dict[key] = sort_keys_with_symbols(value)
        else:
            sorted_dict[key] = value
    return sorted_dict


def generate_diff(d1, d2, formatter='stylish'):
    def compare(a, b):
        result_dict ={}
        for k in a.keys():
            k_plus = f"+ {k}"
            k_minus = f"- {k}"
            if k in b:
                if isinstance(a[k], dict) and isinstance(b[k], dict):
                    nested_diff = compare(a[k], b[k])
                    if nested_diff:
                        result_dict[k] = nested_diff
                elif a[k] == b[k]:
                    result_dict[k] = a[k]
                else:
                    result_dict[k_minus] = a[k]
                    result_dict[k_plus] = b[k]
            else:
                result_dict[k_minus] = a[k]
        for k in b.keys():
            if k not in a:
                k_plus = f"+ {k}"
                result_dict[k_plus] = b[k]
        return sort_keys_with_symbols(result_dict)
    if formatter == 'stylish':
        return format_data(compare(d1, d2), " ", 4)
    else:
        raise ValueError("Unsupported format")
    
    


