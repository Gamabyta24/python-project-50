from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.fjson import format_json


def get_formatter(format_name):
    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }
    if format_name not in formatters:
        raise ValueError(f"Unknown format: {format_name}")
    return formatters[format_name]
