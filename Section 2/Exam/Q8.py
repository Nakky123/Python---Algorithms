import math
n = int(input())
result = '*'.join([str(i) for i in range(1, n + 1)])
print(f"{n}!=({result})={math.factorial(n)}")
