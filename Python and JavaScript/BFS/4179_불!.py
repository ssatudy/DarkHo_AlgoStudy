from collections import deque

def fire_move(r, c):
    next_fire_positions = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == '#' or maze[nr][nc] == 'F':
            continue
        maze[nr][nc] = 'F'
        next_fire_positions.append((nr, nc))
    return next_fire_positions

def person_move(r, c):
    next_person_positions = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] != '.':
            continue
        maze[nr][nc] = maze[r][c] + 1
        next_person_positions.append((nr, nc))
    return next_person_positions

def bfs():
    q = deque(fire_positions)
    q.appendleft(now)
    maze[now[0]][now[1]] = 1
    is_impossible = True
    while q:
        r, c, what = q.popleft()
        if what == 'F':
            next_fire_positions = fire_move(r, c)
            for r, c in next_fire_positions:
                q.append((r, c, 'F'))
            continue
        if maze[r][c] == 'F':
            continue
        if r == 0 or r == R-1 or c == 0 or c == C-1:
            print(maze[r][c])
            is_impossible = False
            break
        next_person_positions = person_move(r, c)
        for r, c in next_person_positions:
            q.append((r, c, 'P'))
    if is_impossible:
        print('IMPOSSIBLE')

R, C = map(int, input().split())
maze = []
fire_positions = []
for r in range(R):
    data = list(input())
    for c in range(C):
        if data[c] == 'F':
            fire_positions.append((r, c, 'F'))
            continue
        if data[c] == 'J':
            now = (r, c, 'P')
    maze.append(data)
bfs()