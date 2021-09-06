# 달팽이
N = int(input())
find_num = int(input())

box = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]  # 상우하좌
dc = [0, 1, 0, -1]
k = 0  # 방향
num = 1  # 시작값
r = N // 2  # 출발 좌표
c = N // 2
cnt = 1
ans_r = 0
ans_c = 0

while num <= N * N:
    for i in range(2):
        for j in range(cnt):
            if box[r][c] == 0:
                box[r][c] = num
            r += dr[k]
            c += dc[k]
            num += 1
            if find_num==1:
                ans_r=N//2+1
                ans_c=N//2+1
            elif num == find_num:
                ans_r = r + 1  # 인덱스를 번호로
                ans_c = c + 1
        k = (k + 1) % 4
    cnt += 1

for i in box:
    print(*i)
print(ans_r, ans_c)