case = int(input())
for _ in range(case):
    data = input()
    left = []
    right = []
    for char in data:
        if char == '<' and left:
            right.append(left.pop())
        elif char == '>' and right:
            left.append(right.pop())
        elif char == '-' and left:
            left.pop()
        elif char not in {'<', '>', '-'}:
            left.append(char)
    if right:
        right.reverse()
    print(''.join(left)+''.join(right))