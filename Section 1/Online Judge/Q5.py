def findOdd(n):
    total = (n*(n+1)//2) ** 2
    return total
num = int(input())
print(findOdd(num))