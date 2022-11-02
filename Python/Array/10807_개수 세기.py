N = int(input())
integer = list(map(int, input().split()))
v = int(input())
ans = 0
for i in range(N):
    if integer[i] == v:
        ans += 1
print(ans)