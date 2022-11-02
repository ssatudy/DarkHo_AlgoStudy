cnt = [0]*26
start = ord('a')

word = input()
for i in range(len(word)):
    cnt[ord(word[i]) - start] += 1
print(*cnt)