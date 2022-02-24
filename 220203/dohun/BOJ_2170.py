import sys

input = sys.stdin.readline
# sys안쓰니깐 안되네..
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

start = arr[0][0]
end = arr[0][1]
cnt = 0

for i in range(1, N):
    # 겹치는경우
    if arr[i][0] <= end < arr[i][1]:
        end = arr[i][1]

    # 안겹치면 길이 측정해서 더해주기
    elif arr[i][0] > end:
        cnt += end - start
        start = arr[i][0]
        end = arr[i][1]

# 안걸리는거 대비 더하기
cnt += (end - start)

print(cnt)