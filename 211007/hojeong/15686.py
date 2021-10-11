# 치킨 배달
def check():
    global ans
    distance=0
    for i in range(N):
        for j in range(N):
            if city[i][j]==1:
                temp=999999
                for r,c in sel:
                    temp=min(temp,abs(i-r)+abs(j-c))
                distance+=temp

    if ans>distance:
        ans=distance

# 조합
def comb(idx, s_idx):
    if s_idx == M:
        check()
        return
    elif idx == l:
        return
    else:
        sel[s_idx] = chicken[idx]
        comb(idx + 1, s_idx + 1)
        comb(idx + 1, s_idx)

N,M=map(int,input().split())
city=[list(map(int,input().split())) for _ in range(N)]
chicken=[]
# 치킨가게 찾기
for r in range(N):
    for c in range(N):
        if city[r][c]==2:
            chicken.append([r,c])
# M개 만큼 뽑기
l=len(chicken)
sel=[0]*M
ans=99999999
comb(0,0)

# 거리합
print(ans)
