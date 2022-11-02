N = int(input())

cnt = [0]*10

while N != 0:
    num = N % 10
    cnt[num] += 1
    N //= 10


cnt[6] = (cnt[6] + cnt[9]) // 2 + 1 if (cnt[6] + cnt[9]) % 2 == 1 else (cnt[6] + cnt[9]) // 2
cnt[9] = 0
print(max(cnt))