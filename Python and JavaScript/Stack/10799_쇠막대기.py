input_data = input()
parenthesis_cnt = len(input_data)       # 괄호 개수
ans = 0                                 # 정답
if parenthesis_cnt != 0:
    stick = 0
    i = 0
    while i <= parenthesis_cnt-1:
        if (input_data[i] == '(' and input_data[i+1] == ')'):       # '()'인 경우 막대기 자르기
            ans += stick                                            # 정답 + 현재 막대 개수
            i += 2                                                  # 인덱스 + 2
            continue
        if input_data[i] == '(':                                    # '('인 경우 정답과 막대 개수 + 1
            ans += 1
            stick += 1
        elif input_data[i] == ')':
           stick -= 1                                               # ')'인 경우 막대 개수 - 1  
        i += 1                                                      # 인덱스 + 1
print(ans)
