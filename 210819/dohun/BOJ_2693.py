N = int(input()) # N번
for i in range(N):
    arr = list(map(int, input().split()))
    # 선택정렬
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[idx] > arr[j]:
                idx = j
        arr[idx], arr[i] = arr[i], arr[idx]

    print(arr[-3])