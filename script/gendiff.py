import argparse
import json

def read_json_file(file_path):
    """Читает и парсит JSON-файл."""
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    
    # Определяем аргументы
    parser.add_argument('first_file', help='первый файл для сравнения')
    parser.add_argument('second_file', help='второй файл для сравнения')
    parser.add_argument('-f', '--format', help='установить формат вывода')
    parser.add_argument('-r', '--read', help='прочитать файл')

    args = parser.parse_args()

    # Чтение и парсинг файлов
    data1 = read_json_file(args.first_file)
    data2 = read_json_file(args.second_file)

    print("Содержимое", args.first_file, ":", data1)
    print("Содержимое", args.second_file, ":", data2)

if __name__ == '__main__':
    main()
