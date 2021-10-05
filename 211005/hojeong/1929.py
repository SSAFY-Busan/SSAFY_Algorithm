# 소수 구하기
def check(n):
    if n==1:
        return False
    k=2
    while k*k<=n:
        if n%k==0:
            return False
        k+=1
    return True

M,N=map(int,input().split())
for i in range(M,N+1):
    if check(i):
        print(i)