# 완전수
T = int(input())  # 개수 입력
num = list(map(int, input().split()))  # 공백 기준 나눠서 리스트
for i in num:  # 리스트 순회
    total = 0  # 총 합 초기화
    for j in range(1, i):  # 1부터 자기자신보다 1작은 수 까지
        if i % j == 0:  # 약수이면
            total += j  # 더해주기
    if total == i:
        print('Perfect')
    elif total < i:
        print('Deficient')
    else:
        print('Abundant')
