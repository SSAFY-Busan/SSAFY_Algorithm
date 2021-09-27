# 에디터
import sys
s = sys.stdin.readline()  # 문자 입력
cursor = len(s)
M = int(sys.stdin.readline())  # 명령어 개수
for i in range(M):
    t = sys.stdin.readline().split()
    r_s=s[cursor:]
    if t[0] == 'L':
        if cursor != 0:
            cursor -= 1
    if t[0] == 'D':
        if cursor != len(s):
            cursor += 1
    if t[0] == 'B' and cursor != 0:
        s = s[0:cursor - 1] + s[cursor:]
        cursor -= 1
    if t[0] == 'P':
        s = s[0:cursor] + t[1] + s[cursor:]
        cursor += 1
print(s)
