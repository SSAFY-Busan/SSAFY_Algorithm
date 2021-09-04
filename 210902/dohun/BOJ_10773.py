import sys

K = int(input())
stack = []

for i in range(K):
    num = int(sys.stdin.readline())
    # 0일 경우 최근 숫자 제거
    if num == 0:
        stack.pop()
    # 아닐경우 추가
    else:
        stack.append(num)

print(sum(stack))