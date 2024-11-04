import json
from script.gendiff import generate_diff
import pytest


@pytest.fixture
def create_json_file(tmp_path):
    """Фикстура для создания временного JSON-файла с заданными данными."""

    def _create_json_file(filename, data):
        file_path = tmp_path / filename
        with open(file_path, "w") as file:
            json.dump(data, file)
        return file_path

    return _create_json_file


def test_no_differences(create_json_file):
    # Одинаковые файлы
    file1 = create_json_file("tf1.json", {"key1": "value1", "key2": "value2"})
    file2 = create_json_file("tf2.json", {"key1": "value1", "key2": "value2"})
    result = generate_diff(str(file1), str(file2))
    expected_output = """{
    key1: value1
    key2: value2
}"""
    assert result.strip() == expected_output.strip()


def test_key_added(create_json_file):
    # Один файл содержит дополнительный ключ
    file1 = create_json_file("tf1.json", {"key1": "value1"})
    file2 = create_json_file("tf2.json", {"key1": "value1", "key2": "value2"})
    result = generate_diff(str(file1), str(file2))
    expected_output = """{
    key1: value1
  + key2: value2
}"""
    assert result.strip() == expected_output.strip()


def test_key_removed(create_json_file):
    # Один файл имеет меньше ключей
    file1 = create_json_file("tf1.json", {"key1": "value1", "key2": "value2"})
    file2 = create_json_file("tf2.json", {"key1": "value1"})
    result = generate_diff(str(file1), str(file2))
    expected_output = """{
    key1: value1
  - key2: value2
}"""
    assert result.strip() == expected_output.strip()


def test_value_changed(create_json_file):
    # Значение одного из ключей изменилось
    file1 = create_json_file("tf1.json", {"key1": "value1", "key2": "value2"})
    file2 = create_json_file("tf2.json", {"key1": "value1", "key2": "new_v"})
    result = generate_diff(str(file1), str(file2))
    expected_output = """{
    key1: value1
  - key2: value2
  + key2: new_v
}"""
    assert result.strip() == expected_output.strip()
