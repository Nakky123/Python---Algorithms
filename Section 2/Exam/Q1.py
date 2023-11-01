import math
def perm(a,b):
    result = math.factorial(a) // math.factorial(a-b)
    return result
a , b = map(int , input().split())
print(perm(a,b))