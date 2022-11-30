N = int(input())
nums = list(map(int, input().split()))
stack = [0] * N
top = -1
ans = [-1]*N

for i in range(N):
    while top != -1 and nums[stack[top]] < nums[i]:
        ans[stack[top]] = nums[i]
        top -= 1
    top += 1
    stack[top] = i

print(*ans)