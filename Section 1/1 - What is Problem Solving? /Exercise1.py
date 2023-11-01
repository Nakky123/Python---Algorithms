def madd(a , b) :
    c = [[0] * m for _ in range(n)]
    for i in range(len(a)):
        for j in range(len(a[0])):
             c[i][j] = a[i][j] + b[i][j]
    return c
def mprint(a):
    for i in range(len(a)):
        print(" ".join(map(str , a[i])))
n , m = map(int , input("Enter row and col : ").split())
a = [list(map(int , input(f"Enter {n} Interger A : ").split())) for _ in range(n)]
b = [list(map(int , input(f"Enter {n} Interger B : ").split())) for _ in range(n)]
c = madd(a , b)
mprint(c)

