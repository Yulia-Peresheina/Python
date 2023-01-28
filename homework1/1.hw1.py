# Найдите сумму цифр трехзначного числа.
number = input("Введите трехзначное число: ")
while number == "" or int(number) > 999 or int(number) < 100:
    number = input("Ошибка. Введите трехзначное число: ")
number = int(number)
sum = 0
while number > 0:
    sum += number % 10
    number = number//10
print(f"Сумма цифр числа составляет {sum}")
