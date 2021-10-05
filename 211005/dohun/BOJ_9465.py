# DP문제
T = int(input())

for tc in range(T):
    N = int(input())

    # 2개의 리스트
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if N == 1:
        print(max(arr1[0], arr2[0]))
    else:
        # 크로스로 더해주기
        arr1[1] += arr2[0]
        arr2[1] += arr1[0]
        for i in range(2, N):
            arr1[i] += max(arr2[i-1], arr2[i-2])
            arr2[i] += max(arr1[i-1], arr1[i-2])

        print(max(arr1[N-1], arr2[N-1]))