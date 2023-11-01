def triple_fibonacci(n):
    FORM = (2**32) - 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        a, b, c = 1, 2, 3
        for _ in range(4, n + 1):
            next_fib = (a + b + c) % FORM
            a, b, c = b, c, next_fib
        return c

N = int(input())
print(triple_fibonacci(N))
