def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
max_length = len(str(factorial(n)))

for i in range(0, n + 1):
    space = 2 if i < 10 else 1
    print(f"{i}! = {factorial(i):>{max_length + space}}")
