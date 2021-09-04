# 달팽이
N = int(input())
key = int(input())

box = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]  # 상우하좌
dc = [0, 1, 0, -1]
d = 0  # 방향

num = 1  # 시작값
r = N // 2  # 출발 좌표
c = N // 2

k=2
while num <= N * N:
    cnt=0
    while cnt<(k//2):
        box[r][c]=num
        if num==key:
            ans=[r+1,c+1] #인덱스에서 번호로
        num+=1
        r+=dr[d]
        c+=dc[d]
        cnt+=1
    d=(d+1)%4
    k+=1

for i in box:
    print(*i)
print(ans[0],ans[1])
