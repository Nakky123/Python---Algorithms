import math
def lcm(x, y):
    return x * y // math.gcd(x, y)

X = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

lcm_value = X[0]
for i in range(len(X)):
    lcm_value = lcm(lcm_value, X[i])
print(lcm_value)
