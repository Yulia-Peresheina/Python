# Напишите функцию same_by(characteristic, objects), 
# которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

values = [0, 2, 10, 8, 62]

def same_by(func, obj):
    if len(set(map(func, obj))) == 1:                                     #вариант с урока
    # if sum(map(func, obj)) == len(obj) or  sum(map(func, obj)) == 0:    #мой вариант
        return True
    return False



if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")

