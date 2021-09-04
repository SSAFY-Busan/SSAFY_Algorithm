N = int(input())
arr = list(map(int, input().split()))
max_value = 0 # 최대값
hap = 0 # 총 합
# 최대값 찾기
for num in arr:
    if max_value < num:
        max_value = num

# 새로운 계산
for num in range(len(arr)):
    hap += arr[num] / max_value * 100
    
print(hap/N)