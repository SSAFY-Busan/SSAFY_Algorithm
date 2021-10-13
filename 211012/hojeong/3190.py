# 뱀
from collections import deque
dr=[0,1,0,-1] # 우 하 좌 상
dc=[1,0,-1,0]

#입력
N=int(input()) # 보드크기
b=[[0]*N for _ in range(N)]

K=int(input()) # 사과개수
for i in range(K):
    r,c=map(int,input().split())
    b[r-1][c-1]=1


L=int(input()) # 방향 변환 횟수
time=[0]*L # 시간
d=[0]*L # 방향
for i in range(L):
    tmp=input().split()
    time[i]=int(tmp[0])
    d[i]=tmp[1]

# 변수
cnt=0 # 게임 시간
k=0 # 현재 방향 (처음은 오른쪽으로 보고 있다)
turn=0 # 변환 인덱스
r,c=0,0 # 출발점
q=deque() # 뱀이 있는 인덱스
q.append([r,c])

while 1:
    # 방향 변경
    if cnt in time:
        if d[turn]=='L':
            k=(k-1)%4
        elif d[turn]=='D':
            k=(k+1)%4
        turn+=1

    # 전진
    cnt+=1
    nr=r+dr[k]
    nc=c+dc[k]
    # 사과
    if nr<0 or nc<0 or nr>=N or nc>=N or [nr,nc] in q:
        break
    elif b[nr][nc]==0:
        q.popleft() # 꼬리 줄이기

    b[nr][nc]=0 # 사과 없애기
    q.append([nr,nc]) # 머리 전진
    r=nr
    c=nc

print(cnt)
