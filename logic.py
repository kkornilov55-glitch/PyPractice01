#Вариант номер 9

import pickle
import json

#1. Что будет результатом следующих выражений?
# "agility"[2:5] + "taxonomy"[3:6]
# int( ''.join( "7/7/07".split('/') ) )
def task1():
    print("agility"[2:5] + "taxonomy"[3:6])
    print(int( ''.join( "7/7/07".split('/') ) ))

#10. Напишите скрипт, выводящий все элементы строки с их номерами
#индексов.
def task2(string):
    for i in range(len(string)):
        print(str(i) + ": " + string[i])

# 21. Напишите скрипт, переводящий список из различного количества
# числовых целочисленных элементов в одно число. Пример списка: [15, 23,
# 150], результат: 1523150
def task3(num_lst):
    print("".join(map(str, num_lst)))

# 26. Напишите скрипт для удаления элемента словаря.
def task4_v1(d, key):
    new_d = dict()
    for k in d:
        if k != key:
            new_d[k] = d[k]
    return new_d

def task4_v2(d, key):
    del d[key]
    return d

#36. Удалите повторяющиеся элементы из списка.
def task5(lst):
    print(list(set(lst)))

#40. Напишите скрипт для добавления текста в файл и отображения
#содержимого файла. Доработайте скрипт и добавьте функцию для чтения
#последних n строк файла.
path = "testFiles/test.txt"
def task6_read(n = -1):
    with open(path, "r", encoding='utf-8') as f:
        lines = f.readlines()

    if n == -1:
        text = ''.join(lines)
    else:
        text = lines[-n:]

    print(''.join(text))

def task6_write(text):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

# 44. Запишите словарь в файл посредством модуля pickle и прочитайте его.
def task7_write(d):
    with open("testFiles/pickleTest.txt", "wb") as f:
        pickle.dump(d, f)

def task7_read():
    with open("testFiles/pickleTest.txt", "rb") as f:
        d = pickle.load(f)
    return d



# 46. Запишите словарь в файл посредством модуля json и прочитайте его.

def task8_write(d):
    with open("testFiles/jsonTest.txt", "w") as f:
        json.dump(d, f)

def task8_read():
    with open("testFiles/jsonTest.txt", "r") as f:
        d = json.load(f)

    for k, v in d.items():
        print(f"{k}: {v}")