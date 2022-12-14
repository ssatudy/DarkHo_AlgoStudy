for _ in range(int(input())):
    data = input()
    stack = []
    stack_length = 0
    ans = 'YES'
    for parenthesis in data:
        if parenthesis == '(':
            stack.append(parenthesis)
            stack_length += 1
            continue
        if stack_length == 0:
            ans = 'NO'
            break
        stack.pop()
        stack_length -= 1
    if stack_length != 0:
        ans = 'NO'
    print(ans)