# 상어 초등학교

dr=[-1,1,0,0]
dc=[0,0,-1,1]

# 좋아하는 학생
def check(num):
    global max_cnt
    global max_like
    for r in range(N):
        for c in range(N):
            cnt=0
            if g[r][c]:
                continue
            elif g[r][c]==0: #자리가 비었다면
                for d in range(4):
                    nr=r+dr[d]
                    nc=c+dc[d]
                    if 0<=nr<N and 0<=nc<N and g[nr][nc] in students[num]:
                        cnt+=1
            if max_cnt<cnt:
                max_cnt=cnt
                max_like=[[r,c]]
            elif max_cnt==cnt:
                max_like.append([r,c])


# 비어있는 칸 체크
def check2():
    global max_cnt2
    global max_close
    for i in range(len(max_like)):
        r=max_like[i][0]
        c=max_like[i][1]
        cnt=0
        for d in range(4):
            nr=r+dr[d]
            nc=c+dc[d]
            if 0<=nr<N and 0<=nc<N and g[nr][nc]==0:
                cnt+=1
        if max_cnt2<cnt:
            max_cnt2=cnt
            max_close=[[r,c]]
        elif max_cnt2==cnt:
            max_close.append([r,c])

# 행,열 정렬
def check3():
    global max_close
    if len(max_close):
        max_close.sort(key=lambda x:(x[0],x[1]))
    else:
        for r in range(N):
            for c in range(N):
                if g[r][c]==0:
                    max_close=[[r,c]]

# 만족도 구하기
def calc():
    total=0
    for r in range(N):
        for c in range(N):
            temp=0
            for d in range(4):
                nr=r+dr[d]
                nc=c+dc[d]
                if 0<=nr<N and 0<=nc<N and g[nr][nc] in students[g[r][c]]:
                    temp+=1
            if temp==4:
                total+=1000
            elif temp==3:
                total+=100
            elif temp==2:
                total+=10
            elif temp==1:
                total+=1
    return total


N=int(input())
students=[0]*(N*N+1)
order=[]
g=[[0]*N for _ in range(N)]

for i in range(N*N):
    temp=list(map(int,input().split()))
    order.append(temp[0])
    students[temp[0]]=temp[1:]

for i in order:
    like = [[0] * N for _ in range(N)]
    close = [[0] * N for _ in range(N)]
    max_like = []
    max_cnt = 0
    max_close = []
    max_cnt2 = 0
    check(i)
    if len(max_like)==1:
        t_r=max_like[0][0]
        t_c=max_like[0][1]
        g[t_r][t_c]=i
    else:
        check2()
        check3()
        t_r = max_close[0][0]
        t_c = max_close[0][1]
        g[t_r][t_c] = i

print(calc())