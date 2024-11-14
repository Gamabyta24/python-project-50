from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import format_json


def get_formatter(format_name):
    """gets a formatter from several options."""
    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }
    if format_name not in formatters:
        raise ValueError(f"Unknown format: {format_name}")
    return formatters[format_name]
