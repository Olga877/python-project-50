import argparse
import json

from gendiff import generate_diff


def parse_files():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args()
    args_dict = vars(args)
    file1 = json.load(open(args_dict.get('first_file')))
    file2 = json.load(open(args_dict.get('second_file')))
    sorted_file1 = dict(sorted(file1.items()))
    sorted_file2 = dict(sorted(file2.items()))
    # print(sorted_file1, sorted_file2)
    print(generate_diff(sorted_file1, sorted_file2))
    return generate_diff(sorted_file1, sorted_file2)

    # dict_list = [{'file1': sorted_file1, 'file2': sorted_file2}]
    # return dict_list
    # print(dict_list)