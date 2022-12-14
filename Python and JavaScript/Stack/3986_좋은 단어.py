def stack_push(alphabet):           # stack에 알파벳을 저장
    global stack_length
    stack_length += 1
    stack.append(alphabet)

def stack_pop():                    # stack에 알파벳을 삭제
    global stack_length
    stack_length -= 1
    stack.pop()

N = int(input())
ans = 0
for _ in range(N):
    word = input()
    stack = []                      # stack
    stack_length = 0                # stack에 저장된 알파벳 개수
    for alphabet in word:
        if stack_length == 0 or alphabet != stack[-1]:      # stack이 비었거나 stack의 마지막에 저장된 알파벳과 다르면 stack에 저장
            stack_push(alphabet)
            continue
        stack_pop()                 # stack의 마지막에 저장된 알파벳과 같으면 저장된 알파벳 삭제
    if stack_length == 0:           # stack이 비었다면 카운팅
        ans += 1
print(ans)