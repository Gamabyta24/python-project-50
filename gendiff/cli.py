import argparse


def parser():
    """Add flags and help output in function"""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file", help="первый файл для сравнения")
    parser.add_argument("second_file", help="второй файл для сравнения")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        choices=["stylish", "plain", "json"],
        help="установить формат вывода (по умолчанию: stylish)",
    )

    return parser.parse_args()
