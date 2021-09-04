N = int(input())
arr = []
cnt = 0 # 뺄 경험치

# 입력받기
for i in range(N):
    arr.append(int(input()))

# 뒤에서부터 돌기
for i in range(N-1, 0, -1):
    # 앞에꺼가 경험치가 더 많으면
    if arr[i] <= arr[i-1]:
        # 차이의 +1을 구한후 빼줘서 원래 경험치를 맞춘다.
        cnt += (arr[i-1] - arr[i] + 1)
        arr[i-1] -= (arr[i-1] - arr[i] + 1)

print(cnt)
