# 자리배정
dr = [0, 1, 0, -1]  # 상우하좌
dc = [1, 0, -1, -0]
d = 0  # 방향
C, R = map(int, input().split())  # C:가로 R:세로
K = int(input())  # 대기 순서

start = [1, 0]  # 0부터 시작한다고 가정
num = 0
flag = False  # 이중 반복문 탈출 변수

if K > C * R:  # 찾는 수가 가로*세로 보다 크면
    print(0)
elif K == 1:  # 찾는 수가 1이면
    print(1, 1)
else:
    # 규칙 찾기
    # 0부터 시작한다고 가정하면 가로가 7 세로가 6일떄
    # 세로는 6 5 4 3 2 1
    # 가로는 6 5 4 3 2 1

    C -= 1
    while 1:
        if flag:
            break
        for i in range(R):
            num += 1
            start[0] += dr[d]
            start[1] += dc[d]
            if num == K:
                flag = True
                break
        d = (d + 1) % 4
        if flag:
            break
        for i in range(C):
            num += 1
            start[0] += dr[d]
            start[1] += dc[d]
            if num == K:
                flag = True
                break
        d = (d + 1) % 4
        R -= 1
        C -= 1
    print(start[0], start[1])
