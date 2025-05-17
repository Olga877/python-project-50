from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff_json():
    expected = read_file("result.txt")
    actual = generate_diff("file1.json", "file2.json")
    assert actual == expected


def test_generate_diff_yml():
    expected = read_file("result.txt")
    actual = generate_diff("file1.yml", "file2.yml")
    assert actual == expected


def test_generate_diff_json_plain():
    expected = read_file("result_plain.txt")
    actual = generate_diff("file1.json", "file2.json", 'plain')
    assert actual == expected


def test_generate_diff_yml_plain():
    expected = read_file("result_plain.txt")
    actual = generate_diff("file1.yml", "file2.yml", 'plain')
    assert actual == expected


def test_generate_diff_json_json():
    expected = read_file("result_json.json")
    actual = generate_diff("file1.json", "file2.json", 'json')
    assert actual == expected


def test_generate_diff_yml_json():
    expected = read_file("result_json.json")
    actual = generate_diff("file1.yml", "file2.yml", 'json')
    assert actual == expected