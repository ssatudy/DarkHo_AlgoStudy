
from collections import deque

def pop_left():
    global N, select_cnt, left_move
    select_cnt += 1
    N -= 1
    move_left(1)

def move_left(cnt):
    global left_move
    left_move += cnt

def move_right(cnt):
    global right_move
    right_move += cnt

N, M = map(int, input().split())
position = list(map(int, input().split()))
check = [0]*N
for i in range(M):
    check[position[i]-1] = i + 1

q = deque(check)
pop_cnt = 0
ans = 0
num = 1
while pop_cnt != M:
    for i in range(N):
        # 꺼내야할 위치 찾기
        if q[i] == num:
            # 회전 방향과 횟수 확인
            if i <= N - i:
                direction = 'left'
                turn_cnt = i
            else:
                direction = 'right'
                turn_cnt = N - i
            # 회전
            if direction == 'left':
                for _ in range(turn_cnt):
                    q.rotate(-1)
            else:
                for _ in range(turn_cnt):
                    q.rotate(1)
            # 다음 위치를 위해 + 1
            num += 1
            # 회전 횟수 저장
            ans += turn_cnt
            q.popleft()
            # 꺼냈으므로 크기 - 1
            N -= 1
            # 꺼낸 횟수 + 1
            pop_cnt += 1
            break
print(ans)