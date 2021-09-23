# 수리공 항승
N, L = map(int, input().split())  # N: 물이 새는 곳의 개수 L: 테이프 길이
point = list(map(int, input().split()))  # 물이 새는 위치
lst = []  # 위치 - 0.5, 위치 +0.5 리스트
for i in point:
    lst.append(i - 0.5)
    lst.append(i + 0.5)
lst.sort()  # 정렬
# [0.5, 1.5, 1.5, 2.5, 99.5, 100.5, 100.5, 101.5]
ans = 0  # 테이프 수
min = 0  # 테이프 붙이는 시작 위치
for i in lst:
    if min < i:
        min = i + L
        ans += 1
print(ans)
