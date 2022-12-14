N = int(input())
for _ in range(N):
    word1, word2 = input().split()
    word_length = len(word1)
    if len(word2) != word_length:
        print('Impossible')
    else:
        start = ord('a')
        first = [0]*26
        second = [0]*26
        for i in range(word_length):
            first[ord(word1[i]) - start] += 1
            second[ord(word2[i]) - start] += 1
        print('Possible' if first == second else 'Impossible')