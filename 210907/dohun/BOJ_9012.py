N = int(input())

for i in range(N):
    stack = []
    words = input()

    # 회전
    for word in words:
        # 여는 괄호면 스택에 추가
        if word == "(":
            stack.append(word)
        # 닫는 괄호면
        elif word == ")":
            # 스택에 없으면 스택에 추가
            if len(stack) == 0:
                stack.append(word)
            # 스택 마지막에 여는괄호면 제거
            elif stack[-1] == "(":
                stack.pop()

    # 스택에 남아있지 않으면 Yes
    if len(stack) == 0:
        print("YES")
    # 아니면 NO
    else:
        print("NO")