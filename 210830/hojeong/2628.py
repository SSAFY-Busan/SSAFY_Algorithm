# 종이 자르기
R, C = map(int, input().split())  # 가로 세로
n = int(input())  # 점선 개수
r = [0, R]  # 가로처음과 끝
c = [0, C]  # 세로처음과 끝

# 자르는 지점 추가
for i in range(n):
    d, k = map(int, input().split())
    if d == 0:  # 가로로 자르면
        c.append(k)  # 세로 길이가 달라짐
    else:
        r.append(k)

r.sort()
c.sort()
l_r = []
l_c = []
# 가로,세로 길이 구하기
for i in range(len(r) - 1):
    l_r.append(r[i + 1] - r[i])
for i in range(len(c) - 1):
    l_c.append(c[i + 1] - c[i])
# 가로,세로 최대 길이 곱하기
max_r = max(l_r)
max_c = max(l_c)
print(max_r * max_c)
