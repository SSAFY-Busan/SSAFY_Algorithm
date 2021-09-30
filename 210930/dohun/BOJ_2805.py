import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N은 나무원의 수  M은 길이

arr = list(map(int, input().split()))
start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2
    tree = 0
    for num in arr:
        if num > mid:
            tree += num - mid

    if tree >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)