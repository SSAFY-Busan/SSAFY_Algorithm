#게임을 만든 동준이
N=int(input()) # 레벨
scores=[]
for i in range(N):
    scores.append(int(input()))
cnt=0
while 1:
    if len(scores)==len(set(scores)) and scores==sorted(scores): #중복이 없고 오름차순이면 멈춰
        break
    for i in range(N-1):
        if scores[i]>=scores[i+1]:
            scores[i]-=1
            cnt+=1
print(cnt)