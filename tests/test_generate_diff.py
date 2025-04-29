import json
from pathlib import Path
import yaml
from yaml.loader import SafeLoader

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff_json():
    file1 = json.load(open("file1.json"))
    file2 = json.load(open("file2.json"))
    sorted_file1 = dict(sorted(file1.items()))
    sorted_file2 = dict(sorted(file2.items()))
    expected = read_file("result.txt")
    actual = generate_diff(sorted_file1, sorted_file2)
    assert actual == expected

def test_generate_diff_yml():
    file1 = yaml.load(open("file1.yml"), Loader=SafeLoader)
    file2 = yaml.load(open("file2.yml"), Loader=SafeLoader)
    sorted_file1 = dict(sorted(file1.items()))
    sorted_file2 = dict(sorted(file2.items()))
    expected = read_file("result.txt")
    actual = generate_diff(sorted_file1, sorted_file2)
    assert actual == expected



def test_generate_diff_json_plain():
    file1 = json.load(open("file1.json"))
    file2 = json.load(open("file2.json"))
    sorted_file1 = dict(sorted(file1.items()))
    sorted_file2 = dict(sorted(file2.items()))
    expected = read_file("result_plain.txt")
    actual = generate_diff(sorted_file1, sorted_file2, 'plain')
    assert actual == expected

def test_generate_diff_yml_plain():
    file1 = yaml.load(open("file1.yml"), Loader=SafeLoader)
    file2 = yaml.load(open("file2.yml"), Loader=SafeLoader)
    sorted_file1 = dict(sorted(file1.items()))
    sorted_file2 = dict(sorted(file2.items()))
    expected = read_file("result_plain.txt")
    actual = generate_diff(sorted_file1, sorted_file2, 'plain')
    assert actual == expected