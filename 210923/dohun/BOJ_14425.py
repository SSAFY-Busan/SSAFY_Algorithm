# N,M은 문자열 개수
N, M = map(int, input().split())

target = [input() for _ in range(N)] # 찾아야할 리스트
lst = [input() for _ in range(M)] # 전체리스트

cnt = 0

for word in lst:
    if word in target:
        cnt += 1

print(cnt)