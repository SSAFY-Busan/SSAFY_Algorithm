while True:
    stack = []
    words = input()
    # 길이가 1개이고 .이면 반복문 종료
    if len(words) == 1 and words[0] == '.':
        break

    for word in words:
        # 여는괄호인 경우 스택에 추가
        if word == '(' or word == '[':
            stack.append(word)

        # 닫는괄호인 경우
        elif word == ')' or word == ']':
            # )일때 스택이 존재하고 스택에 마지막이 여는괄호인 경우
            if word ==')' and stack and stack[-1] == '(':
                stack.pop()
            # ]일때 스택이 존재하고 스택에 마지막이 여는괄호인 경우
            elif word == ']' and stack and stack[-1] == '[':
                stack.pop()
            # 그냥 닫는괄호만 있을 경우 스택에 추가
            else:
                stack.append(word)
        else:
            pass

    # 스택 길이가 0이면 yes
    if len(stack) == 0:
        print("yes")
    else:
        print("no")


