### Hexlet tests and linter status:
[![Actions Status](https://github.com/Gamabyta24/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Gamabyta24/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/64cbc6d8086ea5653313/maintainability)](https://codeclimate.com/github/Gamabyta24/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/64cbc6d8086ea5653313/test_coverage)](https://codeclimate.com/github/Gamabyta24/python-project-50/test_coverage)


# Gendiff

**Gendiff** – это программа, которая определяет разницу между двумя структурами данных.  

###  Поддержка:
- Разные входные форматы: **YAML, JSON**
- Генерация отчета в форматах:  
  - **Plain text**  
  - **Stylish**  
  - **JSON**  

##  Установка

1. Установите **Poetry** (если не установлен).
2. Выполните команду:

   ```sh
   make install

## Запуск

Введите одну из ниже перечисленных команд в зависимости от нужного формата отображения:

   ```sh
   make run-stylish
   make run-plain
   make run-json

## Зависимости

Программа работает с использованием следующих зависимостей:

Python : ^3.10
PyYAML : ^6.0.2
Pytest : ^8.3.3
Pytest-cov : ^6.0.0
Codeclimate-test-reporter : ^0.2.3
