# def solve(cmd,queue) :
#     if cmd[0] == 'enqueue' :
#         queue.append(cmd[1])
#     elif cmd[0] ==  'dequeue' :
#             print('Oops!' if len(queue) == 0 else queue.pop(0))
#     elif cmd[0] == 'peek' :
#         print("None!" if len(queue) == 0 else queue[0])
#     elif cmd[0] == 'size' :
#         print(len(queue))
#     elif cmd[0] == 'empty' :
#         print(len(queue) == 0)


# n = int(input())
# queue = []
# for _ in range(n) :
#     cmd = input().split()
#     solve(cmd,queue)



#================Class====================
from queue import Queue

def solve(cmd,queue) :
    if cmd[0] == 'enqueue' :
        queue.enqueue(cmd[1])
    elif cmd[0] ==  'dequeue' :
            print('Oops!' if queue.empty() else queue.dequeue())
    elif cmd[0] == 'peek' :
        print("None!" if queue.empty() else queue.peek())
    elif cmd[0] == 'size' :
        print(queue.size())
    elif cmd[0] == 'empty' :
        print(queue.empty())

n = int(input())
queue = Queue()
for _ in range(n) :
    cmd = input().split()
    solve(cmd,queue)
