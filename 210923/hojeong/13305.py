# 주유소
# 41점...
N=int(input()) # 도시 개수
km=list(map(int,input().split())) # 도시간 거리
price=list(map(int,input().split())) # 주요소 리터당 가격
price.pop() # 마지막 도시의 주유소 정보는 필요없다
ans=0 # 총 가격
buy=min(price)
l=0
for i in range(N-2,0,-1):
    if price[i]==buy:
        l+=km[i]
        ans+=buy*l
        l=0
        buy=min(price[:i])
    else:
        l+=km[i]
ans+=(l+km[0])*price[0]
print(ans)
