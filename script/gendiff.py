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
    
    # Собираем все ключи из обоих файлов и сортируем их
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    result = []
    
    # Обрабатываем каждый ключ
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        
        # Формируем вывод в зависимости от наличия ключа в каждом из файлов и их значений
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {value1}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {value2}")
        elif value1 != value2:
            result.append(f"  - {key}: {value1}")
            result.append(f"  + {key}: {value2}")
        else:
            result.append(f"    {key}: {value1}")
    
    # Форматируем результат с фигурными скобками и новой строкой после каждого ключа
    result = "{\n" + "\n".join(result) + "\n}"
    return result

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    # Определяем аргументы
    parser.add_argument("first_file", help="первый файл для сравнения")
    parser.add_argument("second_file", help="второй файл для сравнения")
    parser.add_argument("-f", "--format", help="установить формат вывода")
    parser.add_argument("-r", "--read", help="прочитать файл")

    args = parser.parse_args()

    # Чтение и парсинг файлов
    result = generate_diff(args.first_file, args.second_file)
    print(result)

if __name__ == "__main__":
    main()
