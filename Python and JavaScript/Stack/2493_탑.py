N = int(input())
heights = list(map(int, input().split()))
ans = [0]*N
stack = []
for i in range(N-1, -1, -1):
    while stack and heights[stack[-1]] < heights[i]:
        idx = stack.pop()
        ans[idx] = i + 1
    stack.append(i)
print(*ans)