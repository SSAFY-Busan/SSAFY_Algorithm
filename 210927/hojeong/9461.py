# 파도반 수열
T = int(input())
# 설명 그림에 색칠 된 부분과 흰 부분을 따로 생각
# 색칠(a) : 1 1 2 4 7 12
# 흰색(b) : 1 2 3 5 9
# 색칠의 다음은  / 방향으로 더한 값
# 흰색의 다음은 ㅣ 방향으로 더한 값

for tc in range(T):
    N = int(input())
    a = [1, 1]
    b = [1]
    lst = [1, 1, 1]
    if N <= 3:
        print(1)
    else:
        for i in range(3, N):
            if i % 2:
                temp = a[-2] + b[-1]
                b.append(temp)
            else:
                temp = b[-2] + a[-1]
                a.append(temp)
            lst.append(temp)
        print(lst[-1])
