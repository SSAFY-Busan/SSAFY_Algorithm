N = list(map(int, input()))
arr = [0 for _ in range(10)]

# 카운팅
for i in N:
    arr[i] += 1

# 9를 전부 6으로 바꿔준다.
arr[6] += arr[9]
arr[9] = 0
cnt = 0

while True:
    # 합이 0이되면 끝
    if sum(arr) == 0:
        break

    # 6과 9를 제외한 숫자는 전부 1씩 제거
    for i in range(len(arr)):
        if arr[i] > 0 and i != 6:
            arr[i] -= 1
        # 6이나 9면 6을 제거한다.
        elif arr[i] > 0 and i == 6:
            arr[i] -= 1
        elif arr[6] > 0 and i == 9:
            arr[6] -= 1
    # 한바퀴 돌면 +1
    cnt += 1

print(cnt)