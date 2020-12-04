# Gitlab API wrapper

## Установка

1. python3 pip install -r requiements.txt в виртуальном окружении.
2. Добавить токен Гитлаба в .env файл (export TOKEN=[token]).

## Использование

* python3 gitlab.py [method_name] [entities_type] *--file*

***Например:***

* python3 gitlab.py get projects --file myfile
  создаст файл myfile.json

