# Даны два массива чисел. Требуется вывести те
# элементы первого массива (в том порядке,
# в каком они идут в первом массиве),
# которых нет во втором массиве.

# Пользователь вводит число N - количество
# элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива

# list_1 = [int(input(f"Ввести {i} число массива")) for i in range(int(input("сколько чисел? ")))]
# list_2 = [int(input(f"Ввести {i} число массива ")) for i in range(int(input("сколько чисел? ")))]


list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
# альтернатива ввода через map
list_11 = list(map(int, input().split()))
print(list_11)

def dif_list(list_1, list_2):
   # list_3 = list((set(list_1)).difference(set(list_2)))
    for i in list_1:
        if i in list_2:
            list_1.remove(i)
    return list_1

def dif_list1(list_1, list_2):
    list_3 = list((set(list_1)).difference(set(list_2)))
    for i in list_1:
        if i not in list_3:
            list_1.remove(i)
    return list_1
        

print(dif_list(list_1, list_2)) 
print(dif_list1(list_1, list_2)) 


# -------------------------------------------------------------------------------
# Не работает 
# def dif_list(listA, listB):
#     if len(listB) == 0:
#         return
#     listC = []
#     for i in range(len(listA)):
#         for j in range(len(listB)):
#             if listA[i] != listB[j]:
#                 dif_list(listA, listB.remove(listB[j]))
#                 return listC.remove(listA[i])
                
#     return listC

# print(dif_list(list_1, list_2))

# ----------------------------------------------------------------------------------
# генератор списка через not in
# list_C = [list_1[i] for i in  range(len(list_1)) if list_1[i] not in list_2]
# print(list_C)

list_C = [i for i in list_1 if i not in list_2]
print(list_C)