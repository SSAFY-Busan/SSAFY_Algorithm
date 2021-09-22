N = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()

left, right = 0, len(arr)-1
cnt = 0

while left != right:
    if arr[left] + arr[right] == target:
        cnt += 1
        left += 1
    # 타겟보다 크면 숫자가 큰 오른쪽을 한칸 앞으로
    elif arr[left] + arr[right] > target:
        right -= 1
    # 타겟보다 작으면 숫자가 작은 왼쪽을 한칸 뒤로
    else:
        left += 1

print(cnt)