import math
a, b = map(int, input().split())
A = int('1' * a)
B = int('1' * b)
print(math.gcd(A, B))
