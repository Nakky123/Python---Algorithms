def gcd(n,m):
    while m != 0:
        n , m = m , n % m
    return n
a = int(input())
b = int(input())
print(gcd(a, b))