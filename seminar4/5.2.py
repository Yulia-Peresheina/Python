# Проверяем число, простое оно или нет.

def simple_num(n):
    if n in [2, 3]:
        return 'yes'
    elif n == 1 or n % 2 == 0:
        return 'no'
    for i in range(5, n//2 + 1, 2):
        if n % i == 0:
            return 'no'
    return 'yes'

print(simple_num(34))