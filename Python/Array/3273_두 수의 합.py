n = int(input())
nums = set(map(int, input().split()))
x = int(input())
used = set()
ans = 0
for num in nums:
    if num in used:
        continue
    sub = x - num
    if num != sub and sub in nums:
        used.add(x-num)
        ans += 1
print(ans)