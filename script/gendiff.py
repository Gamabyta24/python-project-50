import argparse
from script.build_diff import build_diff
from script.formaters.stylish import format_stylish
from script.formaters.plain import format_plain
from script.formaters.fjson import format_json
from script.pars import read_file


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def main():
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

    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, format_name=args.format)
    print(result)


if __name__ == "__main__":
    main()
