from collections import deque

def bfs():
    stairs = [0] * (F+1)
    stairs[S] = 1
    q = deque()
    q.append(S)
    while q:
        now = q.popleft()
        if now + U <= F and stairs[now+U] == 0:
            stairs[now+U] = stairs[now] + 1
            q.append(now+U)
        if now - D > 0 and stairs[now-D] == 0:
            stairs[now-D] = stairs[now] + 1
            q.append(now-D)
        if stairs[G]:
            print(stairs[G]-1)
            return
    print('use the stairs')

# F: 건물 총 층수, S: 강호의 현재 층수, G: 스타트링크 층수,
# U: 위로 올라갈 수 있는 층수, D: 아래로 내려갈 수 있는 층수
F, S, G, U, D = map(int ,input().split())
bfs()