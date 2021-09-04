# 수 이어가기
def my_cnt(lst):
    cnt = 2
    while 1:
        temp = lst[-2] - lst[-1]  # 끝에서 두번째- 마지막 숫자 빼기
        if temp < 0:  # 음수면 탈출
            break
        lst.append(temp)  # 아니면 추가
        cnt += 1
    return cnt, lst


# 수 이어가기
N = int(input())  # 숫자 입력
ans_cnt = 0  # 카운팅 비교 변수

if N < 5:  # 입력숫자가 5 미만
    result = my_cnt([N, (N + 1) // 2])
    ans_cnt = result[0]
    ans_list = result[1]
else:  # 아니면
    for i in range(N // 5 * 3, N // 5 * 4):  # 이 구간 안에 최대 카운트가 있음
        temp_list = [N, i]
        result = my_cnt(temp_list)
        if result[0] > ans_cnt:
            ans_cnt = result[0]
            ans_list = result[1]
print(ans_cnt)
print(*ans_list)
