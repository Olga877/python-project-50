import argparse
import json

def generate_diff():
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
    dict_list = {'file1': file1, 'file2': file2}
    print(dict_list)