from gendiff.cli import pars
from gendiff.generate_diff import generate_diff


def main():
    args = pars()
    result = generate_diff(args.first_file, args.second_file, format_name=args.format)
    print(result)


if __name__ == "__main__":
    main()
