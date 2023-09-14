from datetime import datetime


def title_data():
    name = input('Введите заголовок заметки: ')
    return name


def body_data():
    surname = input('Введите содержание заметки: ')
    return surname


def time_data():
    return datetime.now().strftime("%Y/%m/%d, %H:%M:%S")


def date_data():
    date_ = input('Введите дату в формате ГГГГ/ММ/ДД: ')
    print()
    return date_
