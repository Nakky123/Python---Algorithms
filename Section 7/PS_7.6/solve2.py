def solve(n,k) :
    queue = [ i for i in range(1, n + 1)]
    j = 0
    while len(queue) > 1 :
        j = (j + k - 1) % len(queue)
        queue.pop(j)
    return queue[0]


N,K = map(int,input().split())
print(solve(N,K))