from collections import deque

def fire_move(r, c):
    next_fire_positions = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= h or nc < 0 or nc >= w or building[nr][nc] == '#' or building[nr][nc] == '*':
            continue
        building[nr][nc] = '*'
        next_fire_positions.append((nr, nc))
    return next_fire_positions

def person_move(r, c):
    global person_cnt
    next_person_positions = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= h or nc < 0 or nc >= w or building[nr][nc] != '.':
            continue
        building[nr][nc] = building[r][c] + 1
        next_person_positions.append((nr, nc))
    return next_person_positions

def bfs():
    q = deque(fire_positions)
    q.appendleft(now)
    building[now[0]][now[1]] = 1
    is_impossible = True
    while q:
        r, c, what = q.popleft()
        if what == 'F':
            next_fire_positions = fire_move(r, c)
            for r, c in next_fire_positions:
                q.append((r, c, 'F'))
            continue
        if building[r][c] == '*':
            continue
        if r == 0 or r == h-1 or c == 0 or c == w-1:
            print(building[r][c])
            is_impossible = False
            break
        next_person_positions = person_move(r, c)
        for r, c in next_person_positions:
            q.append((r, c, 'P'))
    if is_impossible:
        print('IMPOSSIBLE')

test_case = int(input())
for _ in range(test_case):
    w, h = map(int, input().split())
    building = []
    fire_positions = []
    for r in range(h):
        data = list(input())
        for c in range(w):
            if data[c] == '*':
                fire_positions.append((r, c, 'F'))
                continue
            if data[c] == '@':
                now = (r, c, 'P')
        building.append(data)
    bfs()