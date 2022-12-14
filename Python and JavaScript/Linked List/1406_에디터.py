'''
방법 1
단순히 입력받으면 하나씩 실행 => 시간초과
문자열의 길이가 최대 100000에 명령어가 최대 500000개
배열에 50만 번 값을 추가 한다면 최악의 경우 100000 * 500000으로 시간 안에 불가능!!
'''
# word = list(input())
# M = int(input())
# word_length = len(word)
# now = word_length
# for _ in range(M):
#     data = input().split()
#     if data[0] == 'L' and now != 0:
#         now -= 1
#     elif data[0] == 'D' and len(word) > now:
#         now += 1
#     elif data[0] == 'B' and now != 0:
#         now -= 1
#         word.pop(now)
#     elif data[0] == 'P':
#         word.insert(now, data[1])
#         now += 1
# print(''.join(word))

'''
방법2
시간 문제를 해결하기 위해서는 값을 제거하고 추가하는데 O(N) 시간이 걸리지 않도록 해야함
해결 방법 - 2개의 스택을 이용
한 스택은 커서의 왼쪽을 의미
다른 스택은 커서의 오른쪽을 의미
    - 각 스택은 커서와 가까운 쪽이 오른쪽 끝에 오고 커서와 먼 쪽이 왼쪽으로 오게 됨
    - 이렇게 하면 pop()을 하면 커서의 바로 왼쪽과 오른쪽 문자를 꺼낼 수 있음
L의 경우 왼쪽 스택에서 pop()하여 오른쪽 스택에 append
D의 경우 오른쪽 스택에서 pop()하여 왼쪽 스택에 append
B의 경우 왼쪽 스택에서 pop()
P의 경우 왼쪽 스택에 append
    - 추가, 삭제를 O(N)에서 O(1)로 바꿨기 때문에 시간 초과 문제 해결
'''
import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
M = int(input())
for _ in range(M):
    data = list(input().split())
    if data[0] == 'L' and left:
        right.append(left.pop())
    elif data[0] == 'D' and right:
        left.append(right.pop())
    elif data[0] == 'B' and left:
        left.pop()
    elif data[0] == 'P':
        left.append(data[1])
if right:
    right.reverse()
print(''.join(left) + ''.join(right))