# cnt개의 원반을 start에서 end로 옮기는 함수
def hanoi(cnt, start, end, sub):    # cnt: 옮길 원반의 개수,  start: 현재 기둥, end: 목표 기둥, sub: 보조 기둥
    if cnt == 1:                    # 원반의 개수가 1개이면 start에서 end로 옮김
        order.append((start, end))
        return
    hanoi(cnt-1, start, sub, end)   # cnt-1개의 원반을 sub로 옮김
    order.append((start, end))      # 남은 원반을 start에서 end로 옮김
    hanoi(cnt-1, sub, end, start)   # 남은 cnt-1개의 원반을 sub에서 end로 옮김

N = int(input())
order = []                          # 순서를 저장하는 리스트
hanoi(N, 1, 3, 2)
print(len(order))
for start, end in order:
    print(start, end)