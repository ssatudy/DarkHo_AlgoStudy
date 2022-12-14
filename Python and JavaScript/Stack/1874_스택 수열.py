def add():
    global num, top
    num += 1
    top += 1
    stack[top] = num
    ans.append('+')

n = int(input())
stack = [0]*n
top = -1
ans = []
num = 0
isPossible = True
for i in range(n):
    now = int(input())
    if isPossible:
        if top != -1 and stack[top] > now:
            print('NO')
            isPossible = False
            continue
        if top == -1:
            while num != now:
                add()
        elif stack[top] <= now:
            while stack[top] != now:
                add()
        top -= 1
        ans.append('-')
if isPossible:
    for operator in ans:
        print(operator)


