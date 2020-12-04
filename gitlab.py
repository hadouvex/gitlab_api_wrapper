import requests
import json
import os
import argparse
import string

TOKEN = os.environ.get('TOKEN')

projects = {}
namespaces = {}

N_PER_PAGE = 100

### ИСПОЛЬЗОВАНИЕ ###

# python3 gitlab.py [method_name] [entities_type] *--file*
# Например:
# python3 gitlab.py get projects myjsonfile
# Будет создан файл myjsonfile.json с сущностями в формате:
# {id1: {'name1': 'name1'}, id2: 'name2': 'name2'}

# Для работы нужен private_token, его нужно поместить в .env:
# export TOKEN=[private_token]

### ИСПОЛЬЗОВАНИЕ ###

def get_entities(entities_type, entities_dict={}, n=1):
    print(f'getting {entities_type}')
    response = requests.get(f'https://gitlab.com/api/v4/{entities_type}?per_page={N_PER_PAGE}&page={n}&membership=true&private_token={TOKEN}').json()
    print(f'page number: {n};', 'entities on page: ', len(response))
    for i in range(len(response)):
        entities_dict[response[i]['id']] = {'name': response[i]['name']}
    if len(response) == N_PER_PAGE:
        print('ok; appened')
        get_entities(entities_type, entities_dict, n+1)
    return entities_dict

def write_file(file_name, entities_dict):
    try:
        os.remove(f'{file_name}')
        print(f'found old {file_name} file, removed')
        print(f'data was written to a new {file_name} file')
    except:
        print(f"couldn't find {file_name} file, created new: {file_name}.json")

    with open(f'{file_name}.json', 'w') as f:
        json.dump(entities_dict, f)

def get_entities_and_write_to_file(entities_type, file_name):
    write_file(file_name, get_entities(entities_type))

def parse_args():
    parser = argparse.ArgumentParser(description="Gitlab API wrapper")
    parser.add_argument('request_type', type=str, help="request type")
    parser.add_argument('entities_type', type=str, help='projects/groups/etc')
    parser.add_argument('--file', type=str, help='specify file name, otherwise the default will be used')
    args = parser.parse_args()
    if args.file == None:
        args.file = args.entities_type
    return args
    # parser.add_argument('detail_level', type=str, help="min/full")

def validate_args(args):
    allowed_request_types = ['get']
    allowed_entities_types = ['projects', 'namespaces']
    allowed_symbols = set(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    if args.request_type in allowed_request_types and args.entities_type in allowed_entities_types and set(args.file) <= allowed_symbols:
        return True
    else:
        return False

def main():
    args = parse_args()
    if validate_args(args):
        if args.request_type == 'get':
            get_entities_and_write_to_file(args.entities_type, args.file)
    else:
        print('Args are not valid! Exiting...')


if __name__ == '__main__':
    main()
