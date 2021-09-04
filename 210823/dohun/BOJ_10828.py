import sys
input = sys.stdin.readline

N = int(input())
stack = [] # 스택 넣는 곳

for i in range(N):
    x = input().split()
    # push일 경우 숫자를 넣어준다.
    if x[0] == "push":
        stack.append(x[1])

    # pop일 경우 숫자를 빼주는데 비어있을 경우 -1을 출력
    elif x[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    # 사이즈일경우에는 길이 출력
    elif x[0] == "size":
        print(len(stack))

    # 빈공간일 경우 1 출력 아닐경우 0 출력
    elif x[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # top일 경우 스택안에 없으면 -1 출력 아닐 경우 스택 젤 위에꺼 출력
    elif x[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])