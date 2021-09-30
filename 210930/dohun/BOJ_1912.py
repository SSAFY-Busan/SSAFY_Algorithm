# 입력 받기
n = int(input())
array = list(map(int, input().split())) # 배열

# 첫번째 수 입력
dp = [array[0]]
for i in range(n-1):
    # 현재수와 다음수를 합한 수와 다음 수를 비교하여 크기가 큰 수를 계속 추가하며 비교
    dp.append(max(dp[i] + array[i+1], array[i+1]))

print(max(dp))