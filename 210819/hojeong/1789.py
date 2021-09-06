# 수들의 합
# 가장 많은, 다른 자연수의 합들로 표현하기 위해서는 작은 수부터 더해야한다.

S = int(input())

num = 1  # 가장 작은 자연수
total = 0
cnt = 0

while total < S:
    total += num
    num += 1
    cnt += 1

if total == S:
    print(cnt)
else:
    print(cnt - 1)
