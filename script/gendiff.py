import argparse
# import json
# import yaml
# import os
# from script.pars import read_file





# def generate_diff(file1, file2):
    
#     data1 = read_file(file1)
#     data2 = read_file(file2)

#     all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
#     result = []

#     for key in all_keys:
#         value1 = data1.get(key)
#         value2 = data2.get(key)

#         if key in data1 and key not in data2:
#             result.append(f"  - {key}: {value1}")
#         elif key not in data1 and key in data2:
#             result.append(f"  + {key}: {value2}")
#         elif value1 != value2:
#             result.append(f"  - {key}: {value1}")
#             result.append(f"  + {key}: {value2}")
#         else:
#             result.append(f"    {key}: {value1}")

#     result = "{\n" + "\n".join(result) + "\n}"
#     return result


# def main():
#     parser = argparse.ArgumentParser(
#         description="Compares two configuration files and shows a difference."
#     )

#     parser.add_argument("first_file", help="первый файл для сравнения")
#     parser.add_argument("second_file", help="второй файл для сравнения")
#     parser.add_argument("-f", "--format", help="установить формат вывода")
#     parser.add_argument("-r", "--read", help="прочитать файл")

#     args = parser.parse_args()

#     result = generate_diff(args.first_file, args.second_file)
#     print(result)


# if __name__ == "__main__":
#     main()
import json
import yaml
from script.build_diff import build_diff
from script.formaters.stylish import format_stylish
from script.pars import read_file

def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file", help="первый файл для сравнения")
    parser.add_argument("second_file", help="второй файл для сравнения")
    parser.add_argument("-f", "--format", help="установить формат вывода")
    parser.add_argument("-r", "--read", help="прочитать файл")

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()