T = int(input()) # 테스트 케이스

# 처음 갯수
arr = [1, 2, 4]

for i in range(3, 11):
    arr.append(arr[i-1] + arr[i-2] + arr[i-3])

for i in range(T):
    N = int(input())
    print(arr[N-1])