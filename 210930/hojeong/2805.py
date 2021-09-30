# 나무 자르기
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
check = False
st = 0
ed = max(trees)
while st <= ed:
    mid = (st + ed) // 2
    total = 0
    for i in trees:
        if i > mid:
            total += i - mid
    print(mid, st, ed, total)
    if total == M:
        print(mid)
        check = True
        break
    if total > M:  # 낭비하는 나무가 많음-> 높이를 올려야함
        st = mid + 1
    else:  # 나무가 더 필요함 -> 높이를 내려야함
        ed = mid - 1
if check == False:
    print((st + ed) // 2)  # ed
