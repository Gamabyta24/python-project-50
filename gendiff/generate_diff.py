from gendiff.build_diff import build_diff
from gendiff.pars import read_file
from gendiff.formaters import get_formatter


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)

    formatter = get_formatter(format_name)
    return formatter(diff)
