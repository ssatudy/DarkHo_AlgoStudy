N, K = map(int, input().split())

# key = 성별, value = 학년별 인원 수
students = {
    0: [0]*6,
    1: [0]*6
}

# 성별, 학년의 인원 수 카운팅
for i in range(N):
    gender, grade = map(int, input().split())
    students[gender][grade-1] += 1

# 카운팅 수가 K로 나눠떨어지면 몫이 필요한 방의 수, 나눠떨어지지 않으면 몫+1이 필요한 방의 수
ans = 0
for gender in range(2):
    for grade in range(6):
        if students[gender][grade] > 0:
            nums = students[gender][grade]
            if nums % K == 0:
                ans += nums // K
            else:
                ans += nums // K + 1
print(ans)
