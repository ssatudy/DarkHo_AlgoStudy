'''
왼쪽 괄호랑 오른쪽 괄호가 짝을 이루어야 하므로 왼쪽 괄호는 그냥 저장하고 오른쪽 괄호가
나오면 저장된 마지막 괄호와 균형을 이루는지 확인한다.
n = 문장의 개수
s = 문장의 길이
길이가 100글자보다 작으므로 O(s*n)을 예상
'''

left = {'[', '('}               # 왼쪽 괄호
stack = [0]*101                 # 스택
while True:
    sentence = input()
    if sentence == '.':         # .이 오면 종료
        break       
    top = -1                    # 현재 스택의 마지막 위치
    ans = 'yes'
    for char in sentence:
        if char in left:        # 왼쪽 괄호 저장
            top += 1
            stack[top] = char
        elif char == ']':       # 오른쪽 괄호는 저장된 마지막 왼쪽 괄호와 비교
            if top == -1 or stack[top] != '[':
                ans = 'no'
                break
            top -= 1
        elif char == ')':
            if top == -1 or stack[top] != '(':
                ans = 'no'
                break
            top -= 1
    if top != -1:               # 왼쪽 괄호가 남아있으면 no
        ans = 'no'
    print(ans)