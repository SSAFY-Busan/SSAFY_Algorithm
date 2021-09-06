# 참외밭
K = int(input())  # 1제곱미터당 참외 개수
d = []  # 동서남북 1234
l = []  # 변 길이
for i in range(6):  # 6각형
    t_d, t_l = map(int, input().split())
    d.append(t_d)
    l.append(t_l)

long = []  # 2개 긴 변
small = []  # 빼야할 사각형 2 변
for i in range(6):
    if d.count(d[i]) == 1:
        long.append(l[i])

for i in range(6):
    if not l[i] in long:
        if l[(i + 1) % 6] in long or l[i - 1] in long:
            continue
        else:
            small.append(l[i])
box = long[0] * long[1] - small[0] * small[1]
print(box * K)
