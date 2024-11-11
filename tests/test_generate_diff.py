import pytest
from gendiff.generate_diff import generate_diff
import sys
from gendiff.generate_diff import main

file1_path = "files/file1.json"
file2_path = "files/file2.json"

expected_stylish_output = "tests/exp_stylish.txt"
expected_plain_output = "tests/exp_plain.txt"
expected_json_output = "tests/exp_json.txt"


def read_expected_output(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def test_generate_diff_stylish():
    result = generate_diff(file1_path, file2_path, format_name="stylish")
    expect = read_expected_output(expected_stylish_output)
    assert result == expect, "Stylish format output mismatch"


def test_generate_diff_plain():
    result = generate_diff(file1_path, file2_path, format_name="plain")
    expect = read_expected_output(expected_plain_output)
    assert result == expect, "Plain format output mismatch"


def test_generate_diff_json():
    result = generate_diff(file1_path, file2_path, format_name="json")
    expect = read_expected_output(expected_json_output)
    assert result == expect, "JSON format output mismatch"


def test_generate_diff_unknown_format():
    with pytest.raises(ValueError, match="Unknown format: unknown"):
        generate_diff(file1_path, file2_path, format_name="unknown")


def test_main_stylish(monkeypatch, capsys):
    test_args = ["program_name", file1_path, file2_path, "--format", "stylish"]
    expected_output = read_expected_output(expected_stylish_output)

    monkeypatch.setattr(sys, "argv", test_args)
    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_main_plain(monkeypatch, capsys):
    test_args = ["program_name", file1_path, file2_path, "--format", "plain"]
    expected_output = read_expected_output(expected_plain_output)

    monkeypatch.setattr(sys, "argv", test_args)
    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_main_json(monkeypatch, capsys):
    test_args = ["program_name", file1_path, file2_path, "--format", "json"]
    expected_output = read_expected_output(expected_json_output)

    monkeypatch.setattr(sys, "argv", test_args)
    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_main_default_format(monkeypatch, capsys):
    test_args = ["program_name", file1_path, file2_path]
    expected_output = read_expected_output(expected_stylish_output)

    monkeypatch.setattr(sys, "argv", test_args)
    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
