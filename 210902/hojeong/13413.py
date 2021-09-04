# 오셀로 재배치
# 앞면:검정 뒷면:흰색
T = int(input())  # 테스트 케이스 수
for tc in range(T):
    N = int(input())  # 말의 수
    first = input()
    goal = input()
    w = 0  # to w 화이트로 바꿔야 하는 개수
    b = 0  # to b 블랙으로 바꿔야 하는 개수
    for i in range(N):
        if first[i] != goal[i]:
            if goal[i] == 'B':  # 블랙으로 바꿔야 할 경우
                b += 1
            else:
                w += 1
    if w == b:  # 개수가 같다면 서로 바꾸면 됨
        ans = w
    elif w > b:  # w:3 b:2-> 2개는 서로 바꾸고 1는 뒤집는다 .b+(w-b)=w
        ans = w
    else:
        ans = b
    print(ans)
