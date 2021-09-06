from math import gcd
#가로수
N=int(input()) #기존 가로수 수
pos=[int(input()) for _ in range(N)]
# 간격 최대공약수 구하기

l=[] #간격 리스트
for i in range(N-1):
    l.append(pos[i+1]-pos[i])
max_num=gcd(*l) #최대공약수
ans=0
for i in l:
    ans+=i//max_num-1
print(ans)
