# 괄호
T = int(input())  # 테스트케이스 입력
for tc in range(T):
    s = list(input())  # 문자열 리스트로 입력
    cnt = 0
    ans = 'YES'  # 조건에 안걸리면 YES로 출력을 위해 초기값 설정
    for i in s:
        if i == '(':  # 여는 괄호가 나오면 카운트 1증가
            cnt += 1
        else:  # 아니면 1감소
            cnt -= 1
        if cnt < 0:  # 어느순간 카운트가 음수가 되면 여는괄호보다 닫는괄호가 많은 거니깐 NO로 갱신하고 멈춤
            ans = 'NO'
            break
    else:  # 반복문을 다 돌았는데 카운트가 0이 아니면 여는 괄호, 닫는 괄호 개수가 다른거니깐 NO 갱신
        if cnt != 0:
            ans = 'NO'
    print(ans)
