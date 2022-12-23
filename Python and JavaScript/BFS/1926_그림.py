from collections import deque

# dr: 세로 방향, dc: 가로 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 연결된 그림을 모두 확인하고 그림의 사이즈 확인
def bfs(r, c):
    # queue를 활용하여 bfs를 돌림
    q = deque()
    # 0으로 방문 확인
    paper[r][c] = 0
    # 기본 사이즈 1로 초기화
    size = 1
    q.append((r, c))
    # queue가 남아있는 동안 반복
    while q:
        # queue에서 하나씩 꺼내서 확인
        r, c = q.popleft()
        # 상,하,좌,우 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나면 다음 위치 확인
            if nr < 0 or nr >= n or nc < 0 or nc >= m or paper[nr][nc] != 1:
                continue
            paper[nr][nc] = 0       # 방문 처리
            q.append((nr, nc))      # queue에 추가
            size += 1
    return size                     # 최종 그림 사이즈 반환

n, m = map(int, input().split())    # n: 세로 크기, m: 가로 크기
paper = [list(map(int, input().split())) for _ in range(n)]     # 도화지 정보
max_picture_size = 0                # 그림 최대 크기
picture_cnt = 0                     # 그림 개수
for r in range(n):
    for c in range(m):
        if paper[r][c] != 1:        # 그림이 아니면 넘어감
            continue
        # 최대 그림 크기를 저장
        max_picture_size = max(max_picture_size, bfs(r, c))
        picture_cnt += 1            # 그림 개수 카운팅
print(picture_cnt)
print(max_picture_size)