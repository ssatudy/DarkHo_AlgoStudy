cnt = [0]*10
multiply = 1
for i in range(3):
    multiply *= int(input())

while multiply != 0:
    num = multiply%10
    cnt[num] += 1
    multiply //= 10

for i in range(10):
    print(cnt[i])