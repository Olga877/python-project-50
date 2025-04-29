import argparse
import json
import yaml
from yaml.loader import SafeLoader

from gendiff import generate_diff


def parse_files():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output", default='stylish')
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict.get('first_file')[-2 :] and args_dict.get('second_file')[-2 :] == 'ml':
        file1 = yaml.load(open(args_dict.get('first_file')), Loader=SafeLoader)
        file2 = yaml.load(open(args_dict.get('second_file')), Loader=SafeLoader)
        sorted_file1 = dict(sorted(file1.items()))
        sorted_file2 = dict(sorted(file2.items()))
        print(generate_diff(sorted_file1, sorted_file2, args.format))
        return generate_diff(sorted_file1, sorted_file2, args.format)

    else:

        file1 = json.load(open(args_dict.get('first_file')))
        file2 = json.load(open(args_dict.get('second_file')))

        sorted_file1 = dict(sorted(file1.items()))
        sorted_file2 = dict(sorted(file2.items()))
        print(generate_diff(sorted_file1, sorted_file2, args.format))
        return generate_diff(sorted_file1, sorted_file2, args.format)