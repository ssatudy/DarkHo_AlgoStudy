from collections import deque
N, K = map(int, input().split())
people = deque(range(1, N+1))
ans = []
for _ in range(N):
    people.rotate(-(K-1))
    ans.append(str(people.popleft()))
print('<' + ', '.join(ans) + '>')