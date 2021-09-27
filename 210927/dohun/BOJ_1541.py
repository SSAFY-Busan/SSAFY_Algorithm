# 최소가 나오려면 +들끼리 먼저 더한 후 마이너스 해줘야 한다.

number = input().split('-')
num_lst = []

# 마이너스 기준으로 분리
for i in number:
    cnt = 0
    # 플러스 기준으로 더해주기
    a = i.split('+')
    for j in a:
        cnt += int(j)
    num_lst.append(cnt)

cnt_sum = num_lst[0]
for i in range(1,len(num_lst)):
    cnt_sum -= num_lst[i]
print(cnt_sum)

