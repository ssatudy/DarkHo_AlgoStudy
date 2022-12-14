from collections import deque

T = int(input())
for _ in range(T):
    commands = input()
    n = int(input())
    nums = input().lstrip('[').rstrip(']').split(',')
    q = deque(nums)

    direction = 1                   # 1이면 정상(popleft), -1이면 뒤집힌 것(pop)
    errorAtive = False              # 에러 발생 여부
    for command in commands:
        if command == 'R':
            direction *= -1
        else:
            if n == 0:
                errorAtive = True
                break
            else:
                if direction == 1:
                    q.popleft()
                else:
                    q.pop()
                n -= 1
    if errorAtive:
        print('error')
    else:
        nums = list(q)
        if direction > 0:
            print('[' + ','.join(nums) + ']')
        else:
            print('[' + ','.join(nums[::-1]) + ']')