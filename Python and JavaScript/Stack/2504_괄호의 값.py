def check(parenthesis):             # 닫는 괄호인 경우 유효성 검사 후 계산
    global stack_length
    # 소괄호: 2, 대괄호 : 3
    parenthesis_value = 2 if parenthesis == ')' else 3
    # stack의 길이가 0이거나 괄호가 매칭되지 않는다면 False
    if stack_length == 0 or (parenthesis == ')' and stack[-1] == '[') or (parenthesis == ']' and stack[-1] == '('):
        return False

    # stack의 마지막에 숫자가 저장되어 있다면 해당 숫자 더해서 저장
    nums_sum = 0
    while stack[-1] != '(' and stack[-1] != '[':
        stack_length -= 1
        nums_sum += stack.pop()
    
    # 괄호가 매칭되는 경우
    if (parenthesis == ')' and stack[-1] == '(') or (parenthesis == ']' and stack[-1] == '['):
        stack.pop()
        # nums_sum이 있다면 괄호값을 곱해서 저장하고 없다면 괄호값만 저장
        if nums_sum:
            stack.append(nums_sum*parenthesis_value)
        else:
            stack.append(parenthesis_value)
        return True
    return False

input_data = input()            # 입력받은 데이터
stack = []                      # 저장되는 stack
stack_length = 0                # stack 길이
ans = 0                         # 정답

for parenthesis in input_data:
    if parenthesis == '(' or parenthesis == '[':        # 여는 괄호인 경우 stack에 저장
        stack.append(parenthesis)
        stack_length += 1
        continue

    if check(parenthesis):                              # 유효성 검사를 통과하면 괄호가 남아있는지 확인
        if stack[0] != '(' and stack[0] != '[':         # 남은 괄호가 없다면 값을 꺼내서 따로 저장
            ans += stack.pop()
            stack_length -= 1
        continue
    ans = 0
    break
print(ans)