import sys
input = sys.stdin.readline
K = int(input())
nums = [0]*K
top = -1
for _ in range(K):
    num = int(input())
    if num == 0:
        top -= 1
    else:
        top += 1
        nums[top] = num
print(sum(nums[:top+1]))