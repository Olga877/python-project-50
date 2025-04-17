import json
from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff():
    file1 = json.load(open("file1.json"))
    file2 = json.load(open("file2.json"))
    sorted_file1 = dict(sorted(file1.items()))
    sorted_file2 = dict(sorted(file2.items()))
    expected = read_file("result.txt")
    actual = generate_diff(sorted_file1, sorted_file2)
    assert actual == expected