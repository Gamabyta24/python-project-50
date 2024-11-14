from gendiff.build_diff import build_diff
from gendiff.reader import read_file
from gendiff.formaters import get_formatter


def generate_diff(file_path1, file_path2, format_name="stylish"):
    """Returns formated diff list"""
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)

    formatter = get_formatter(format_name)
    return formatter(diff)
