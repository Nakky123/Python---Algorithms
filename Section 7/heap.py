from heapq import heappush, heappop

# This is a heap queue that print all the push all at once
# def solve(cmd, heap, pops):
#     if cmd[0] == "push":
#         heappush(heap, -int(cmd[1]))  
#     elif cmd[0] == "pop":
#         pops.append(0 if not heap else -heappop(heap))

# N = int(input())
# heap = []
# pops = []

# for _ in range(N):
#     cmd = input().split()
#     solve(cmd, heap, pops)

# for pop in pops:
#     print(pop, end=' ')


def solve(cmd, heap):
    if cmd[0] == "push":
        heappush(heap, -int(cmd[1])) 
    elif cmd[0] == "pop":
        print(0 if not heap else -heappop(heap))

N = int(input())
heap = []
for _ in range(N):
    cmd = input().split()
    solve(cmd , heap)