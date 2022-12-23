from collections import deque

first_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
second_move = [[(-1, -1), (-1, 1)], [(1, -1), (1, 1)], [(-1, -1), (1, -1)], [(-1, 1), (1, 1)]]

# 처음 4방향으로 움직이는 함수(r: 현재 행, c: 현재 열, idx: 반복 인덱스)
def find_first_move_position(r, c, idx):
    nr = r + first_move[idx][0]
    nc = c + first_move[idx][1]
    return nr, nc

# 최종 도착 위치를 찾아서 갈 수 있는지 확인하는 함수(r: 한 번 움직인 행, c 한번 움직인 열, idx: 반복 인덱스)
def find_possible_positions(r, c, idx):
    possible_positions = []                     # 도착 가능한 위치를 담을 리스트
    for dr, dc in second_move[idx]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= chess_pan_length or nc < 0 or nc >= chess_pan_length:
            continue
        if visited[nr][nc]:
            continue
        possible_positions.append((nr, nc))     # 도착 가능한 위치면 추가
    return possible_positions

def bfs(r, c):          # bfs로 목표 위치에 도달하는 이동 횟수를 찾는 함수(r: 시작 행, c: 시작 열)
    visited[r][c] = 1   # 방문 처리(재방문 하지 않기 위해)
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()                                              # 현재 위치
        for i in range(4):
            nr, nc = find_first_move_position(r, c, i)                  # 처음 이동한 후 위치
            possible_positions = find_possible_positions(nr, nc, i)     # 최종 위치 리스트
            for nr, nc in possible_positions:                           # 방문 처리 및 queue 추가
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
        if visited[target_row][target_col]:                             # 목표 위치에 도달하면 출력 후 종료
            print(visited[target_row][target_col]-1)
            return

test_case = int(input())
for case in range(test_case):
    chess_pan_length = int(input())                                     # 체스판 길이
    now_row, now_col = map(int, input().split())                        # 현재 위치
    target_row, target_col = map(int, input().split())                  # 목표 위치
    visited = [[0] * chess_pan_length for _ in range(chess_pan_length)] # 방문처리를 위한 리스트
    bfs(now_row, now_col)                                               # 이동 시작