# 큐
import sys

N = int(input())  # 명령의수
q = []
for i in range(N):
    order = sys.stdin.readline().split()
    if len(order) == 2:  # push 인 경우
        q.append(order[1])
    elif order[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
