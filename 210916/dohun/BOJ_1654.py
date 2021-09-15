K, N = map(int, input().split())
# K는 가지고 있는 랜선의 개수, N은 필요한 랜선의 개수

lst = [int(input()) for _ in range(K)]
start, end = 1, max(lst)

while start <= end:
    mid = (start + end) // 2
    line_cnt = 0
    for i in lst:
        line_cnt += i // mid

    print(line_cnt)
    if line_cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)