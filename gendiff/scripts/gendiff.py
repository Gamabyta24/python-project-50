from gendiff.cli import parser
from gendiff.generator import generate_diff


def main():
    args = parser()
    result = generate_diff(args.first_file, args.second_file, format_name=args.format)
    print(result)


if __name__ == "__main__":
    main()
