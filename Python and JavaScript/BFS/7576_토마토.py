from collections import deque

def check_tomatoes_status():        # 토마토 입력, 상태 확인 및 저장
    global tomato_cnt, ripened_tomato_cnt
    for r in range(N):
        tomato_row = list(map(int, input().split()))        # 토마토 입력
        for c in range(M):                                  # 상태 확인
            if tomato_row[c] == -1:
                continue
            elif tomato_row[c] == 1:
                ripened_tomato_cnt += 1
                ripened_tomatoes_positions.append((r, c))   # 익은 토마토의 위치
            tomato_cnt += 1
        tomatoes.append(tomato_row)                         # 저장

def is_all_tomatoes_ripened():                  # 모든 토마토가 익었는지 확인하는 함수
    if ripened_tomato_cnt == tomato_cnt:
        return True
    return False

def find_date(ripened_tomatoes_positions):  # 익을 수 있는 토마토가 모두 익는데 걸리는 시간을 찾는 함수(bfs)
    global ripened_tomato_cnt
    q = deque(ripened_tomatoes_positions)
    date = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:                       # 4방향 확인
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or tomatoes[nr][nc] != 0: # 유효성 검사
                continue
            tomatoes[nr][nc] = tomatoes[r][c] + 1       # 방문 처리
            ripened_tomato_cnt += 1
            q.append((nr, nc))                          # queue에 추가
            date = tomatoes[nr][nc] - 1
    return date

M, N = map(int, input().split())            # M: 가로(열), N: 세로(행)

tomatoes = []                               # 상자에 담긴 토마토
ripened_tomatoes_positions = []             # 익은 토마토 위치
tomato_cnt = 0                              # 전체 토마토 개수
ripened_tomato_cnt = 0                      # 익은 토마토 개수

check_tomatoes_status()                     # 토마토 입력, 상태 확인 및 저장
                                            # 처음부터 모든 토마토가 익었는지 상태 확인
is_all_totatoes_ripened = is_all_tomatoes_ripened()

if is_all_totatoes_ripened:                 # 처음부터 모든 토마토가 있었으면 0 출력
    print(0)
else:
    date = find_date(ripened_tomatoes_positions)   # 토마토가 익는데 걸리는 시간 확인
    if is_all_tomatoes_ripened():
        print(date)
    else:
        print(-1)