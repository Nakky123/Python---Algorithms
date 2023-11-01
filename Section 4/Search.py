def seqsearch(target, n, s):
    for i in range(n):
        if s[i] == target:
            return i
    return -1

def solve(n, m, s, x):
    for i in range(m):
        print(seqsearch(x[i], n, s), end=" ")
    print()

N , M = map(int , input().split())
S = list(map(int , input().split()))
X = list(map(int , input().split()))
solve(N, M, S, X)