first = [0]*26
second = [0]*26

a = ord('a')
word1 = input()
for i in range(len(word1)):
    first[ord(word1[i]) - a] += 1
word2 = input()
for i in range(len(word2)):
    second[ord(word2[i]) - a] += 1

ans = 0
for i in range(26):
    if first[i] == second[i]:
        continue
    elif first[i] > second[i]:
        ans += first[i] - second[i]
    else:
        ans += second[i] - first[i]
print(ans)