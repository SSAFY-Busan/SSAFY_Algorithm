# 연속합
n = int(input())
lst = list(map(int, input().split()))
max_sum = lst[0]  # 최대값
temp = 0  # 누적합 전보다 작아지면 0으로 초기화 (음수상관없음)
ssum = 0  # 누적합 음수면 0으로 초기화
for i in lst:
    temp += i
    ssum += i
    if temp < ssum:
        temp = ssum
    if ssum < 0:  # 누적합이 음수가 나오면 이전의 숫자는 포함안해야함
        ssum = 0
    if max_sum <= temp:  # 지금 누적합이 전의 누적합보다 크면
        max_sum = temp  # 최대값 갱신
    else:
        temp = 0
print(max_sum)
