# N은 물 새는곳, L은 테이프 길이
N, L = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

start = 0 # 시작점
cnt = 0 # 테이프 개수

for i in arr:
    if start < i:
        # 붙이기 시작점부터 테이프 길이를 더하고 0.5줘야하므로 1개전까짐만 커버가 가능
        start = i + L - 1
        cnt += 1

print(cnt)