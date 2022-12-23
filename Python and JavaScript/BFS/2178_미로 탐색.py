queue = [0]*(100*100)                   # queue
dr = [-1, 1, 0, 0]                      # 세로 방향
dc = [0, 0, -1, 1]                      # 가로 방향

def bfs(r, c):                          # bfs로 탐색
    maze[r][c] = 2                      # 방문 처리
    front = -1                          # front: queue의 가장 앞 요소 이전 인덱스
    rear = 0                            # rear: queue의 가장 마지막 요소 인덱스
    queue[rear] = (r, c)
    while front != rear:                # front == rear: queue가 비어있는 상태
        front += 1
        r, c = queue[front]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or maze[nr][nc] != '1':
                continue
            maze[nr][nc] = maze[r][c] + 1
            if maze[N-1][M-1] != '1':       # 원하는 위치에 도착하는 경우 반환
                return maze[N-1][M-1] - 1   # 시작할 때 2로 시작했으므로 반환할때 -1
            rear += 1
            queue[rear] = (nr, nc)
    # return 0                              # 항상 도착할 수 있는 경우만 있으므로 고려X

N, M = map(int, input().split())        # N: 세로(행), M: 가로(열)
maze = [list(input()) for _ in range(N)]
print(bfs(0, 0))
