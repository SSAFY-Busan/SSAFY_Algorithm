n=6
times=[7,10]
times.sort()
check=[False]*len(times)
answer=0
while n:
    for i in range(len(times)):
        if not check[i]:
            if (times[i-1]-answer%times[i-1])+times[i-1]>times[i]:
                n-=1
                check[i]=True
                answer+=times[i]-answer%times[i]
            else:
                answer+=1
                break
        if answer%times[i]==0:
            check[i]=False
        else:
            check[i]=True
print(answer)