




def generate_diff(a, b):
    diff = ''
    for k in a.keys():
        if k in b and a[k] == b[k]:
            diff += f'    {k}: {a[k]}\n'
        elif k in b and a[k] != b[k]:
            diff += f'  - {k}: {a[k]}\n  + {k}: {b[k]}\n'
        elif k not in b:
            diff += f'  - {k}: {a[k]}\n'
    added_keys = b.keys() - a.keys()
    for key in added_keys:
        diff += f'  + {key}: {b[key]}\n'
    print('{\n' + diff + '}')