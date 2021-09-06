# 제로
import sys
K=int(input())
stack=[]
for i in range(K):
    n=int(sys.stdin.readline())
    if n!=0:
        stack.append(n)
    else:
        stack.pop()
ans=sum(stack)
print(ans)