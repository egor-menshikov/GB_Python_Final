from data_create import name_data, surname_data, phone_data, address_data
from datetime import datetime
import json

PATH = 'notebook.json'


def print_data():
    with open(PATH, 'r', encoding='utf-8') as file:
        notebook = json.load(file)
    print()
    for k, v in notebook.items():
        print(f'{k:^2} {v["name"]:<12} {v["surname"]:<14} {v["phone"]:<16} {v["address"]:<16}')
    return notebook


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    note = {'name': name, 'surname': surname, 'phone': phone, 'address': address}

    with open(PATH, 'r', encoding='utf-8') as file:
        notebook = json.load(file)
    for i in range(1, len(notebook) + 2):
        if str(i) not in notebook.keys():
            notebook[i] = note
            break
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(notebook, file, ensure_ascii=False, indent="")


def edit_data():
    notebook = print_data()

    print(note_choice := input('Введите номер записи, которую вы хотите изменить: '))
    while True:
        if note_choice.isdigit() and 0 < int(note_choice) <= len(notebook):
            print(f'\nВы хотите изменить:\n\n'
                  f'{notebook[note_choice]["name"]:<12}'
                  f' {notebook[note_choice]["surname"]:<14}'
                  f' {notebook[note_choice]["phone"]:<16}'
                  f' {notebook[note_choice]["address"]:<16}')
            break
        else:
            print('Вы ошиблись при выборе.')
            print(note_choice := input('Введите номер записи, которую вы хотите изменить: '))
    print(f'{"1) Имя":<12}'
          f' {"2) Фамилия":<14}'
          f' {"3) Телефон":<16}'
          f' {"4) Адрес":<16}')

    print(column_choice := int(input('\nВыберите соответствующую категорию: ')))
    while True:
        match column_choice:
            case 1:
                notebook[note_choice]["name"] = name_data()
                break
            case 2:
                notebook[note_choice]["surname"] = surname_data()
                break
            case 3:
                notebook[note_choice]["phone"] = phone_data()
                break
            case 4:
                notebook[note_choice]["address"] = address_data()
                break
            case _:
                print('Вы ошиблись при выборе.')
                print(column_choice := int(input('\nВыберите соответствующую категорию: ')))

    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(notebook, file, ensure_ascii=False, indent="")


def delete_data():
    notebook = print_data()
    print(note_choice := input('Введите номер записи, которую вы хотите удалить: '))
    notebook.pop(note_choice)
    note_list = [v for k, v in notebook.items()]
    notebook = {str(k): v for k, v in enumerate(note_list, 1)}
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(notebook, file, ensure_ascii=False, indent="")


def search_data():
    with open(PATH, 'r', encoding='utf-8') as file:
        notebook = json.load(file)
    print(prompt := input('\nЧто вы хотите найти?\n-> ').casefold())
    for k, v in notebook.items():
        for value in v.values():
            if prompt in value.casefold():
                print(f'{k:^2} {v["name"]:<12} {v["surname"]:<14} {v["phone"]:<16} {v["address"]:<16}')
                break
