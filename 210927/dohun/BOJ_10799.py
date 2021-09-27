# 스택 문제

stick = list(input())

stack = []
cnt = 0
for num in range(len(stick)):
    if stick[num] == '(':
        stack.append(stick[num])

    else:
        if stick[num-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
