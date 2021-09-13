# 좋은 단어
N = int(input())  # 단어 수
ans = 0  # 좋은 단어 개수
for i in range(N):
    s = list(input())  # 문자 입력
    if len(s) % 2:  # 글자수가 홀수면
        continue  # 넘어감
    lst = [s.pop()]  # 비교 리스트
    while s:
        k = s.pop()
        if len(lst) == 0:
            lst.append(k)
        elif k == lst[-1]:
            lst.pop()
        else:
            lst.append(k)
    if len(lst) == 0:  # 모든 글자가 쌍을 이루고 선이 겹치지 않으면
        ans += 1
print(ans)
