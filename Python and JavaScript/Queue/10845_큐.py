import sys
input = sys.stdin.readline

# def queue_push(num):
#     global rear
#     rear += 1
#     q[rear] = num
#
# def queue_pop():
#     global front
#     front += 1
#     return q[front]
#
# def queue_size():
#     return rear - front
#
# def queue_empty():
#     if front == rear:
#         return 1
#     else:
#         return 0
#
# def queue_front():
#     return q[front+1]
#
#
# def queue_back():
#     return q[rear]
#
# N = int(input())
# q = [0]*10000
# front = rear = -1
#
# for _ in range(N):
#     data = input().split()
#     if data[0] == 'push':
#         queue_push(int(data[1]))
#
#     elif data[0] == 'pop':
#         if queue_empty():
#             print(-1)
#         else:
#             print(queue_pop())
#
#     elif data[0] == 'size':
#         print(queue_size())
#
#     elif data[0] == 'empty':
#         print(queue_empty())
#
#     elif data[0] == 'front':
#         if queue_empty():
#             print(-1)
#         else:
#             print(queue_front())
#
#     elif data[0] == 'back':
#         if queue_empty():
#             print(-1)
#         else:
#             print(queue_back())
import sys
from collections import deque
input = sys.stdin.readline
q = deque()
N = int(input())

for _ in range(N):
    data = input().split()
    if data[0] == 'push':
        q.append(int(data[1]))

    elif data[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif data[0] == 'size':
        print(len(q))

    elif data[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif data[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])