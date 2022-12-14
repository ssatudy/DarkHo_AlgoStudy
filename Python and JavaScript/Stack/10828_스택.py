import sys
input = sys.stdin.readline

N = int(input())
nums = [0]*N
top = -1

for _ in range(N):
    data = input().split()
    if data[0] == 'push':
        top += 1
        nums[top] = data[1]
    elif data[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(nums[top])
            top -= 1
    elif data[0] == 'size':
        print(top+1)
    elif data[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif data[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(nums[top])