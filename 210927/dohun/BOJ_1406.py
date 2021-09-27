# 스택 문제
# 커서 이동 방식으로 하니 시간초과가 난다.

import sys
input = sys.stdin.readline

words = list(input().strip())
T = int(input())
stack = []

# 커서는 맨 뒤에 위치
for i in range(T):
    comm = list(input().split())

    # 커서를 왼쪽으로 이동시키지 않고 따로 빼준다.
    if comm[0] == 'L':
        if words:
            stack.append(words.pop())

    # 커서가 오른쪽이면 스택에 제일 마지막에 들어온 걸 다시 맨뒤로 넣어준다.
    elif comm[0] == 'D':
        if stack:
            words.append(stack.pop())

    # 맨뒤에꺼 삭제
    elif comm[0] == 'B':
        if words:
            words.pop()

    # 추가
    elif comm[0] == 'P':
        words.append(comm[1])

# 반대로 들어가기 때문에 역순으로 추가해줘야함
# 리버스도 가능...
words.append(''.join(stack[::-1]))

print(''.join(words))