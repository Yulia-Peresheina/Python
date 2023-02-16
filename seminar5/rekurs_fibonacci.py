# Найти n-е число фибоначчи

def fib(n):
    if n in [0, 1]:
        return 1
    res = fib(n - 1) + fib(n - 2)
    return res


n = int(input())
print(fib(n))

# 1 1 2 3 5 8 13 21 