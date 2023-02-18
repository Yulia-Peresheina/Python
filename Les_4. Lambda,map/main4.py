# Стандартное описание функций

def calc1(a):
    return a + a

def calc2(a):
    return a * a

def math(op, arg):     # Можем передать финкцию - финкции
    print(op(arg))

math(calc2, 5)

# --------------------------------------------------------
# Использование Лямбда

calc3 = lambda a: a + a
calc4 = lambda a, b: a + b


def math1(op, arg1, arg2):    
    print(op(arg1, arg2))

math1(calc4, 5, 45)
# Использование лямбда непосредственно в другой функции:

math1(lambda c, d: c + d, 6, 7)

# ------------------------------------------------------

spisok = [1, 2, 3, 5, 8, 15, 23, 38]
result = []
for i in spisok:
    if i % 2 == 0:
        result.append((i, i * i))
print(result)
# ------------------------------------------------------
# Вариант 2 используя лямбду

def select(f,col):                        # функция применяет функцию к аргументу 
    return [f(x) for x in col]            #(каждому элементу списка, к примеру)

def where(f, col):                         #Функция выводит каждый элемент если
    return [x for x in col if f(x)]        # условие внутренней функции выполняется

spisok = [1, 2, 3, 5, 8, 15, 23, 38]       #задаем список
res = select(int, spisok)                  # Переводим список в int?
print(res)                 
res = where(lambda x: x % 2 == 0, res)     #элемент выводится, если выполняется условие лямбда-функции
print(res)
res = select(lambda x: (x, x ** 2), res)   # функция для каждого элемента запускает лямбда-функцию
print(res)

sp1 =list(map(int, spisok))
print(sp1)
sp2 = list(map(lambda x: (x, x**2), list(filter(lambda x: x % 2 == 0, sp1))))
print(sp2)