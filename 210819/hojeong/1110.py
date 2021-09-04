# 더하기 사이클

# 숫자가 한자리수이면 앞에 0 붙이는 함수
def checkNum(a):
    if int(a) < 0:
        num = '0' + a
    else:
        num = a

    return num


N = input()  # 입력받은 숫자
origin = checkNum(N)  # 처음 숫자 저장(원래 수로 돌아왔는지 비교하기 위한 변수)
cnt = 0  # 카운팅 변수

while 1:
    cnt += 1
    pre_num = checkNum(N)  # 한자리이면 0붙이기
    num_sum = str(int(pre_num[0]) + int(pre_num[1]))  # 각자리수 합을 구하고 문자열로 반환(인덱스로 접근하기위해)
    result_num = pre_num[-1] + num_sum[-1]  # 오르쪽 숫자를 더한 숫자 반환(문자열로 반환)
    if result_num == origin:  # 그결과가 처음 숫자와 같은지 비교
        break  # 같으면 탈출
    N = result_num  # N에 얻은 숫자를 넣어 다시 반복

print(cnt)
