# 빙고
def find_bingo():
    cnt = 0
    # 행의 합이 0인 경우
    for i in range(5):
        if sum(my_box[i]) == 0:
            cnt += 1

    # 열의 합이 0인 경우
    for i in range(5):
        sum_c = 0
        for j in range(5):
            sum_c += my_box[j][i]
        if sum_c == 0:
            cnt += 1

    # 대각선 합이 0인 경우
    sum_d = 0
    for i in range(5):
        sum_d += my_box[i][i]
    if sum_d == 0:
        cnt += 1

    sum_rd = 0
    for i in range(4, -1, -1):
        sum_rd += my_box[4 - i][i]
    if sum_rd == 0:
        cnt += 1
    return cnt


# 문제시작
my_box = [list(map(int, input().split())) for _ in range(5)]
tell = [list(map(int, input().split())) for _ in range(5)]
num = 1  # 숫자 카운트

flag = False  # 반복문 탈출 조건 변수
for h in range(5):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if tell[h][i] == my_box[j][k]:
                    my_box[j][k] = 0
                    break
        if find_bingo() >= 3:  # 3개 이상일 경우 빙고!
            print(num)
            flag = True
            break
        else:
            num += 1
    if flag:
        break
