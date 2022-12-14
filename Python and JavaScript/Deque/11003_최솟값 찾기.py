# 방법 1
import heapq                                    # 시간 초과 - deque으로 할 수 있으면 deque 쓰기!!!
N, L = map(int, input().split())
input_arr = list(map(int, input().split()))     # 입력받은 숫자 배열
min_nums = []                                   # 꺼내서 저장해둔 숫자 배열(최솟값이 앞에 오도록 heapq 사용)
ans = [0]*N
for i in range(1, N+1):
    start = i - L + 1
    heapq.heappush(min_nums, (input_arr[i-1], i))
    while min_nums[0][1] < start:               # 범위에 벗어나면 버리기
        heapq.heappop(min_nums)
    ans[i-1] = min_nums[0][0]
print(*ans)

# 방법 2
from collections import deque                   
N, L = map(int, input().split())
input_arr = list(map(int, input().split()))
q = deque()
ans = [0]*N
for i in range(1, N+1):
    start = i - L + 1
    while q and q[0][1] < start:                # 인덱스 순서로 넣었기 때문에 앞에서 부터 범위 확인
        q.popleft()
    while q and q[-1][0] > input_arr[i-1]:      # 현재 넣으려는 값과 비교해 큰 숫자는 제거
        q.pop()
    q.append((input_arr[i-1], i))               # 현재 값 추가
    ans[i-1] = q[0][0]                          # 범위 내에서 가장 작은 값이 앞으로 위치되어 있음
print(*ans)