from itertools import combinations

# N은 세로, M 치킨
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 0은 빈칸, 1은 집, 2는 치킨 집
home_lst = []
chicken_lst = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home_lst.append([i,j])
        elif graph[i][j] == 2:
            chicken_lst.append([i,j])

min_value = float('inf')
for num in combinations(chicken_lst, M):
    hap = 0
    for home in home_lst:
        hap += min([abs(home[0]-i[0]) + abs(home[1]-i[1]) for i in num])
        if min_value <= hap:
            break
    if hap < min_value:
        min_value = hap

print(min_value)