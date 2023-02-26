# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле. У каждой записи должна быть id. 
# Id должно проставляться автоматически.
# 
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os
import shutil 

from os import path           # из модуля os импортируем подмодуль path    


file_base = "base.txt"                             # файл как глобальная переменная,
                                                   # и что нужно, с ней все делаем
all_data = []                                      # переменная для считывания данных,
                                                   #  чтобы можно было ее везде использовать 
id = 1

if not path.exists(file_base):                     #Проверяем, есть ли база
                                                   # то есть, есть ли сам файл в системе. 
                                                   # Если нет, создаем его, 
                                                   # если есть - с ним работаем (пропуская это условие)

    with open(file_base, "w", encoding="utf-8") as _:     #имя совершенно не нужно, нам его нужно просто записать
        pass



# ВЫВОД ВСЕХ ЗАПИСЕЙ
def read_records():                                # Предфункция считывания данных для последующего их красивого
                                                   # отображения в функции show_all
    global all_data, id                              # считываем данные в глобальную переменную, чтобы ее можно было менять
    with open(file_base) as f:
        if not f:
            print("No data!")
        else:
            all_data = [i.strip() for i in f]
            id = all_data[-1][0]                       # ссылка на текущую id. обращаемся к последней записи [-1]
                                                   # и дергаем из нее нулевой элемент [0] 

        # return f.readlines()                     # возвращает данные с \n, нужно чистить
        return all_data


def show_all():                                    # Подфункция main_menu. Красивое отображение считанных данных. 
                                                   # Нужна предфункция для считывания данных. это read_records будет

    print(*all_data, sep="\n") 


# -----------------------------------------------------------------------
# ДОБАВЛЕНИЕ ЗАПИСИ

def adding ():
    global all_data, id
    add_id = int(id) + 1
    with open(file_base, "a", encoding="utf-8") as f:
        new_name = input("Write new name: ").upper()
        new_phone = input("Write new phone number: ")
        f.write(f"{add_id} {new_name} {new_phone}\n")
    return print("Done!")

        

def add_new():
    flag = True
    while flag:
        answer = input("Press:\n"
                        "1 - to add a new record \n"
                        "2 - to return to main menu \n")
        match answer:
            case "1":
                adding()
            case "2":
                flag = False
            case _:
                print("Try again!\n")
# ------------------------------------------------------------------------
# ПОИСК ЗАПИСИ
def search_by_name(string):
    global all_data
    count = 0
    result = []
    for i in all_data:
        if string in i:
            result.append(count)
        count += 1
    return result

def search_record():
    os.system('CLS')
    want_find = input("Enter some information: ").upper()
    list_find = search_by_name(want_find)
    if list_find == []:
        print("Not found!")
    else:
        print(*[all_data[i] for i in list_find], sep='\n')

# -------------------------------------------------------------------------
# ИЗМЕНИЕ ЗАПИСИ
def changing(num):
    new_name = input("Write name: ").upper()
    new_phone = input("Write new phone number: ")
    changed_line = num+" "+new_name+" "+new_phone
    return changed_line

def change_record():
    show_all()
    global id
    answer = input(f"Do you know the line for change? \n"
        "1 - Yes\n"
        "2 - No\n")
    match answer:
        case "1":
            line_to_change = input("Enter the line: ")
        case "2":
            line_to_change = search_record()
            if len(line_to_change) > 1:
                line_to_change = input("Choose correct number of line: ")
            elif len(line_to_change) == 0:
                print("Not found!")
    new_string = changing(line_to_change)

    all_data[int(line_to_change) - 1] = new_string
    with open(file_base, 'w') as f:
        for i in all_data:
            f.write(i + "\n")
    print("Done!")
# --------------------------------------------------------------------------
def delete_record():
    
    print("ALL PHONE BOOK")
    show_all()
    num_line = int(input("Which line do you want to delete? "))    
    with open(file_base) as f:
        lines = f.readlines()
    with open(file_base, 'w') as f:
        ch_id = 1
        for line in lines:
            if line.strip('\n') != lines[num_line - 1].strip('\n'):
                line= line.split()
                line[0] = str(ch_id)
                line = " ".join([i for i in line]) + "\n"
                f.write(line)
                ch_id += 1
        print("Done!")

# -----------------------------------------------------------------------------
# Экспорт файла
def export_file():
    new_file_name = input("Enter the name of creating file: ")
    if path.exists(new_file_name):
        print("File exixts!")
    else:
        shutil.copyfile(file_base, new_file_name)
        print("Done!")

# -----------------------------------------------------------------------------
# импорт файла
def import_file():
    importing_file = input("Enter the name of importing file: ")
    if not path.exists(importing_file):
        print("File not exixts!")
    else:
        file_base = importing_file
        print("Done!")
    
# -----------------------------------------------------------------------------
def main_menu():                                   # Создаем функцию меню с подфункциями меню. Не использовать рекукрсию.
    play = True                                    # Создаем переменную-флаг, которая будет использоваться длдя нашего цикла
    while play:
        read_records()
        

        answer = input("Phone book: \n"            # Запускаем бесконечный цикл, передаем
                                                   # информацию пользователю, предлагая ему варианты
                        "1. Show all records.\n"   # Показать все записи
                        "2. Add a new record.\n"   # Добавить новую запись
                        "3. Search a record.\n"    # Найти нужную запись по параметрам
                        "4. Change a record.\n"    # Изменить запись
                        "5. Delete a record.\n"    # Удалить запись8
                        "6. Import the file.\n"             # Импорт данных
                        "7. Export the file.\n"             # Экспорт данных
                        "8. Exit.\n" )             # Завершить работу программы
                                                   
                                         
        match answer:
            case "1":
                os.system('CLS')
                show_all()
            case "2":
                os.system('CLS')
                add_new()
            case "3":
                os.system('CLS')
                search_record()
            case "4":
                os.system('CLS')
                change_record()  
            case "5":
                os.system('CLS')
                delete_record()
            case "6":
                os.system('CLS')
                import_file()
            case "7":
                os.system('CLS')
                export_file()
            case "8":
                play = False
            case _:                               #обработка ввода не корректного ответа
                print("Try again!\n")
main_menu()
