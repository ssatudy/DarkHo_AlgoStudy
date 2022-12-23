from collections import deque

def visited(now, next):                                # 방문처리 함수
    jido[next] = jido[now] + 1
    q.append(next)

def walk_or_teleport(now):                             # 걷거나 순간이동하는 함수
    if 0 <= now-1 and jido[now - 1] == 0:              # 왼쪽으로 걸어갈 수 있는 경우
        visited(now, now - 1)
    if now+1 <= 100000 and jido[now + 1] == 0:         # 오른쪽으로 걸어간 위치에 가본적 없는 경우
        visited(now, now + 1)
    if now * 2 <= 100000 and jido[now * 2] == 0:       # 순간이동 가능하고 가본적 없는 경우
        visited(now, now * 2)

N, K = map(int, input().split())        # N: 수빈이 위치, M: 동생 위치
jido = [0]*100001                       # 지도(방문 여부)
jido[N] = 1                             # 수빈이 위치 방문 표시
q = deque()                             # bfs를 위한 queue
q.append(N)                             # 현재 수빈이 위치를 queue에 추가
while q:
    now = q.popleft()                   # 현재 위치
    walk_or_teleport(now)               # 이동
    if jido[K]:                         # 도착한 경우 출력
        print(jido[K] - 1)
        break