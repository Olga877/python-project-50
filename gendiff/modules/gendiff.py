from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain_formatter import format_plain
from gendiff.formatters.stylish_formatter import format_stylish
import json

import yaml
from yaml.loader import SafeLoader

def get_sorted_files(file_path1, file_path2):
    first_file_extension = file_path1[-2:]
    second_file_extension = file_path2[-2:]
    if first_file_extension and second_file_extension == 'ml':
        file1 = yaml.load(open(file_path1), Loader=SafeLoader)
        file2 = yaml.load(open(file_path2), Loader=SafeLoader)
        sorted_file1 = dict(sorted(file1.items()))
        sorted_file2 = dict(sorted(file2.items()))
    else:
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))
        sorted_file1 = dict(sorted(file1.items()))
        sorted_file2 = dict(sorted(file2.items()))
    return sorted_file1, sorted_file2

def generate_diff(file_path1, file_path2, formatter='stylish'):
    file_path1, file_path2 = get_sorted_files(file_path1, file_path2)
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
        return format_stylish(compare(file_path1, file_path2), " ", 4)
    elif formatter == 'plain':
        return format_plain(compare(file_path1, file_path2))
    elif formatter == 'json':
        return format_json(compare(file_path1, file_path2))
    else:
        raise ValueError("Unsupported format")
    
    


