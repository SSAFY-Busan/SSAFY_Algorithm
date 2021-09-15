N = int(input())
N_arr = list(map(int, input().split()))
sort_lst = sorted(N_arr)

M = int(input())
M_arr = list(map(int, input().split()))

def binary(target):
    left = 0
    right = N-1

    while left <= right:
        mid = (left + right) // 2
        if sort_lst[mid] == target:
            return True

        if target < sort_lst[mid]:
            right = mid - 1
        elif target > sort_lst[mid]:
            left = mid + 1

for i in range(M):
    if binary(M_arr[i]):
        print(1)
    else:
        print(0)