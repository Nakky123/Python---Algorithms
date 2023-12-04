import sys
sys.setrecursionlimit(10**7)

# def solve(n,k) :
#     if n == 1 :
#         return 1
#     else: 
#         return ((solve(n-1,k) + k - 1) % n) + 1
    
def solve2(n,k) :
    f = 1
    for i in range(1,n + 1) :
        f = ((f + k - 1) % i) + 1
    return f
    
N,K = map(int,input().split())
# print(solve(N,K))
print(solve2(N,K))