N = int(input()) # 도시의 개수

distance = list(map(int, input().split()))
money = list(map(int, input().split()))

price = 0 # 비용
cnt = money[0] # 첫번째 주유소 비용

for i in range(N-1):
    # 금액이 작은 주유소가 있으면 갱신
    if money[i] < cnt:
        cnt = money[i]
    # 계속 비용 더해주기
    price += cnt * distance[i]

print(price)