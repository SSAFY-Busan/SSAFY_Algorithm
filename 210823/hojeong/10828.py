#스택
import sys
N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    command=sys.stdin.readline().split()
    word=command[0]
    if word=='push':
        value = command[1]
        stack.append(value)
    elif word == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif word == 'size':
        print(len(stack))
    elif word == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif word == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
