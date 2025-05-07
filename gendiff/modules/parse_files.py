import argparse

from gendiff import generate_diff


def parse_files():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output",
                        default='stylish')
    args = parser.parse_args()

    args_dict = vars(args)
    file_path1 = args_dict.get('first_file')
    file_path2 = args_dict.get('second_file')
    print(generate_diff(file_path1, file_path2, args.format))
    return generate_diff(file_path1, file_path2, args.format)