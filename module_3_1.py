# Домашняя работа по уроку "Пространство имён"

calls = 0  # объявление переменной входа calls


def count_calls():
    global calls  # объявление глобальной переменной
    calls += 1  # увеличение calls
    return calls


def string_info(string):  # объявление функции string_info с параметром string
    count_calls() # обращение к функции count_calls(calls) для подсчета количества входов
    sumbol = len(string)  # определение длины параметра string
    upp = string.upper()  # перевод в верхний регистр параметра string
    low = string.lower()  # перевод в нижний регистр параметра string
    string = (sumbol, upp, low)  # объявление кортежа
    return string  # возвращаемый результат функции


def is_contains(string, list_to_search):  # объявление функции is_contains с параметрами string, list_to_search
    count_calls() # обращение к функции count_calls(calls) для подсчета количества входов
    if string.lower() in str(list_to_search).lower():  # проверка вхождения string с нижним регистром
        # в преобразованном в строку list_to_search с нижним регистром
        arg = True  # string входит в list_to_search
    else:
        arg = False  # string не входит в list_to_search
    return arg  # возвращаемый результат функции


# Исходные данные для функций и результат
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
