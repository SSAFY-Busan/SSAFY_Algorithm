N = int(input())
cnt = 0 # 카운트 횟수
answer = N # 정답 저장

while True:
    num1 = N // 10
    num2 = N % 10
    num3 = num1 + num2
    cnt += 1
    # 10이상일 경우
    if num3 >= 10:
        N = int(str(num2) + str(num3 % 10))
    # 아닐경우
    else:
        N = int(str(num2) + str(num3))
    # 초기 숫자랑 같을경우 종료
    if answer == N:
        break

print(cnt)