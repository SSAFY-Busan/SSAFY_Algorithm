N = int(input())
idx = 1 # 시작 숫자
check_num = False # 체크
stack = [] # 스택
answer = [] # 기호저장 리스트

# 개수만큼 입력 받기
for i in range(N):
    # 숫자만큼 수 입력받기
    num = int(input())
    # idx에서 해당숫자까지 스택에 숫자 넣으면서 + 추가해주기
    while idx <= num:
        stack.append(idx)
        answer.append('+')
        idx += 1

    # 스택 마지막 수랑 입력받은 수가 일치하면 제거해주며 - 추가해주기
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    # 아닐경우 No출력하며 종료
    else:
        print("NO")
        check_num = True
        break

    # No일 경우 그대로 종료
    if check_num == True:
        break

if check_num == False:
    for i in answer:
        print(i)