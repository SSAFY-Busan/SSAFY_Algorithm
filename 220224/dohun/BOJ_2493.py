import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))
stack = []
answer = []

for i in range(len(arr)):
    while True:
        # 스택에 없으면 값을 추가해주기
        if len(stack) == 0:
            stack.append((i, arr[i]))
            answer.append(0)
            break

        # 스택 마지막 값보다 현재값이 작으면
        if stack[-1][1] >= arr[i]:
            answer.append(stack[-1][0]+1)
            stack.append((i, arr[i]))
            break
        else:
            stack.pop()

print(*answer)