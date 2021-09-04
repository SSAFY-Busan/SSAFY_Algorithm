import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x = input().split()

    # push면 큐에 넣는다.
    if x[0] == 'push':
        lst.append(int(x[1]))

    # 사이즈 출력
    elif x[0] == "size":
        print(len(lst))

    # 비어있으면 1 아니면 0출력
    elif x[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    # pop이면 가장 앞에 정수를 출력하고 제외
    elif x[0] == "pop":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
            lst.pop(0)

    # 가장 앞에 정수 출력
    elif x[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])

    # 가장 뒤에 정수 출력
    elif x[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])