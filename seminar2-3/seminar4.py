# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# a a a b c a a d c d d

# Мой вариант:
# list_1 = input().split()
# list_2 = list()
# for i in list_1:
#     if list_1.count(i) > list_2.count(i):     
#         if list_2.count(i) == 0:
#             print(f"{i} ", end='')
#         else:
#             print(f"{i}_{str(list_2.count(i))} ", end='')
#         list_2.append(i)

# Вариант Александра (ученик)
# string = input().split()

# for i in range(len(string)):
#     count = 1
#     for j in range(i + 1, len(string)):
#         if string[i] == string[j]:
#             string[j] += "_" + str(count)
#         count += 1
# print(string)


# Решение со словарем
# string = input().split()
# D = {}.fromkeys(string, 0)
# for i in string:
#     print(f"{i}_{D[i]}" if D[i] else i, end=" ")  # если D[i] true (т.е. значение ключа != 0)
#                                                   #выводим на печать конструкцию слева,
#                                                   #если D[i] false(т.е. значение ключа = 0)
#                                                   #выводим на печать i  
#     D[i] += 1                                     # увеличиваем значение i-го ключа на единицу

# ЗАДАЧА2.

# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним
# или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
# She sells sea shells on the sea shore The shells that she 
# sells are sea shells I'm sure.So if she sells sea shells 
# on the sea shore I'm sure that the shells are sea shore shells

# Длинное решение
# text = input().lower().split()
# text = set(text)
# print(text)
# print(len(text))

# Короткое решение
# print(len(set(input().lower().split())))

# ЗАДАЧА 3
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.



# n = int(input())                            
# # max_number = 1000
# max_number = n
# while n != 0:
#     n = int(input())
#     # if max_number > n:
#     if max_number < n:
#         max_number = n
# print(max_number)



n = int(input())
max_number = -1
# while n < 0:
while n > 0:
    n = int(input())
    if max_number < n:
        # n = max_number
        max_number = n

#print(n)
print(max_number)