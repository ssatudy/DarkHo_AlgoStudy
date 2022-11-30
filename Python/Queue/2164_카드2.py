from collections import deque
q = deque(list(range(1, int(input())+1)))
i = len(q)
while i != 1:
    q.popleft()
    i -= 1
    q.append(q.popleft())
print(q.popleft())
