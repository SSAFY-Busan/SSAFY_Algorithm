# 두 수의 합
import sys

N = int(input())
n = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())
st, ed = 0, N - 1
ans = 0
while st < ed:
    temp = n[st] + n[ed]
    if temp < x:  # 구하는 숫자보다 작으면
        st += 1  # 스타트 인덱스 +1
        continue
    elif temp == x:  # 같으면
        ans += 1  # 1증가
    ed -= 1  # 같을 경우와 구하는 숫자보다 큰 경우 끝 인덱스 1 감소
print(ans)
