# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

number_toys = int(input("Сколько журавликов сделали дети? "))
katya = number_toys//6*4
boys = number_toys//6 
print(f"Катя сделала {katya}, а мальчики по {boys} каждый")