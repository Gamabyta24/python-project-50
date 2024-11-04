import argparse
import json


def read_json_file(file_path):
    """Читает и парсит JSON-файл."""
    with open(file_path, "r") as file:
        return json.load(file)


def generate_diff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    result = []

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key not in data2:
            result.append(f"  - {key}: {value1}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {value2}")
        elif value1 != value2:
            result.append(f"  - {key}: {value1}")
            result.append(f"  + {key}: {value2}")
        else:
            result.append(f"    {key}: {value1}")

    result = "{\n" + "\n".join(result) + "\n}"
    return result


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
