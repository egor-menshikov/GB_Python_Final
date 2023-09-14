from notebook import input_data, print_data, edit_data, delete_data, print_note, search_by_date


def print_menu():
    print('\nМеню:\n'
          '1. Добавить заметку\n'
          '2. Удалить заметку\n'
          '3. Редактировать заметку\n'
          '4. Вывести все заметки\n'
          '5. Вывести заметку по id\n'
          '6. Поиск заметок по дате\n'
          '7. Выход')


def interface():
    command = -1
    while command != 7:
        print_menu()
        command = int(input("Введите номер операции: "))

        while command < 1 or command > 7:
            print('Вы ошиблись при выборе.')
            command = int(input("Введите номер операции: "))

        if command == 1:
            input_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            edit_data()
        elif command == 4:
            print_data()
        elif command == 5:
            print_note()
        elif command == 6:
            search_by_date()
        elif command == 7:
            print("Всего доброго!")
