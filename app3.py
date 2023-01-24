def getNthFib(n):
    current = 3
    fibonaccis = [0, 1]

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        while current <= n:
            new_fib = fibonaccis[current - 2] + fibonaccis[current - 3]
            fibonaccis.append(new_fib)
            current += 1
        return new_fib


print(getNthFib(100))
