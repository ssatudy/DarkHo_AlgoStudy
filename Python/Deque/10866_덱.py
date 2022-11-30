import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    data = input().split()
    command_word = data[0]

    if command_word == 'push_front':
        q.appendleft(data[1])
    elif command_word == 'push_back':
        q.append(data[1])
    else:
        q_size = len(q)
        if command_word == 'size':
            print(q_size)
            continue
        if q_size:
            if command_word == 'empty':
                print(0)
            elif command_word == 'pop_front':
                print(q.popleft())
            elif command_word == 'pop_back':
                print(q.pop())
            elif command_word == 'front':
                print(q[0])
            elif command_word == 'back':
                print(q[-1])
        else:
            if command_word == 'empty':
                print(1)
            else:
                print(-1)
