from logic import *

# --- Словарь для тестов сериализации и удаления ---
sample_dict = {"Имя": "Кирилл", "Курс": 2, "Город": "Тверь"}


# --- Вспомогательная функция для ввода списка чисел ---
def get_int_list(prompt):
    while True:
        try:
            raw = input(prompt)
            # Заменяем запятые на пробелы для удобства
            raw = raw.replace(',', ' ')
            return [int(x) for x in raw.split()]
        except ValueError:
            print("Ошибка! Введите целые числа через пробел.")


# --- МЕНЮ ---
main_menu = """
                 МЕНЮ
    -------------------------------
    1. Базовые операции
    2. Работа с текстовым файлом
    3. Сериализация
    -------------------------------
    0. Выход
    Ваш выбор:
"""

base_operations_menu = """
              БАЗОВЫЕ ОПЕРАЦИИ
    -------------------------------------
    1. Вычислить тестовые выражения
    2. Вывести символы с индексами
    3. Преобразовать список в одно число
    4. Удалить ключ из словаря
    5. Удалить дубликаты из списка
    -------------------------------------
    0. Назад
    Ваш выбор:
"""

# (Добавлен пункт 2 и 0)
text_file_menu = """
         РАБОТА С TXT ФАЙЛОМ
    -------------------------------
    1. Добавить текст в файл
    2. Прочесть весь файл
    3. Прочесть файл (N строк)
    -------------------------------
    0. Назад
    Ваш выбор:
"""

ser_menu = """
              СЕРИАЛИЗАЦИЯ
    ----------------------------------
    Через Pickle
    1. Сохранить словарь
    2. Загрузить словарь
    ----------------------------------
    Через JSON
    3. Сохранить словарь
    4. Загрузить словарь
    ----------------------------------
    0. Назад
    Ваш выбор:
"""

while True:
    print(main_menu)
    try:
        main_choice = int(input())
    except ValueError:
        print("Пожалуйста, введите число!")
        continue

    match main_choice:
        case 0:
            print("Завершение работы...")
            break

        case 1:  # Базовые операции
            while True:
                print(base_operations_menu)
                try:
                    sub_choice = int(input())
                except ValueError:
                    continue

                if sub_choice == 0: break

                match sub_choice:
                    case 1:
                        task1()
                    case 2:
                        s = input("Введите строку: ")
                        task2(s)
                    case 3:
                        lst = get_int_list("Введите числа через пробел (например, 15 23 150): ")
                        task3(lst)
                    case 4:
                        key = input(f"Введите ключ для удаления из {sample_dict}: ")
                        # Используем копию словаря, чтобы оригинал не менялся навсегда
                        temp_dict = sample_dict.copy()
                        print("Результат (v2):", task4_v2(temp_dict, key))
                    case 5:
                        lst = get_int_list("Введите числа через пробел: ")
                        task5(lst)
                    case _:
                        print("Нет такого пункта!")

        case 2:  # Работа с файлом
            while True:
                print(text_file_menu)
                try:
                    sub_choice = int(input())
                except ValueError:
                    continue

                if sub_choice == 0: break

                match sub_choice:
                    case 1:
                        text = input("Введите текст для добавления: ")
                        task6_write(text)
                        print("Текст успешно добавлен!")
                    case 2:
                        task6_read()
                    case 3:
                        try:
                            n = int(input("Сколько последних строк показать? "))
                            task6_read_n(n)
                        except ValueError:
                            print("Нужно ввести число!")
                    case _:
                        print("Нет такого пункта!")

        case 3:  # Сериализация
            while True:
                print(ser_menu)
                try:
                    sub_choice = int(input())
                except ValueError:
                    continue

                if sub_choice == 0: break

                match sub_choice:
                    case 1:
                        task7_write(sample_dict)
                        print("Словарь сохранен через Pickle!")
                    case 2:
                        print('--- Словарь из pickle ---')
                        print(task7_read())
                    case 3:
                        task8_write(sample_dict)
                        print("Словарь сохранен через JSON!")
                    case 4:
                        print('--- Словарь из json ---')
                        task8_read()
                    case _:
                        print("Нет такого пункта!")

        case _:
            print("Нет такого пункта в главном меню!")

    print("\n" + "=" * 40 + "\n")  # Разделитель между действиями