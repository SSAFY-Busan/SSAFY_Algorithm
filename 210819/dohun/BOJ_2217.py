N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

# 선택정렬
for i in range(len(lst) - 1):
    idx = i
    for j in range(i + 1, len(lst)):
        if lst[idx] > lst[j]:
            idx = j
    lst[idx], lst[i] = lst[i], lst[idx]

# 높은 순서에서 갯수 파악해서 최대 중량 파악하기
max_value = 0
for i in range(N-1, -1, -1):
    x = lst[i] * (N-i)
    if x > max_value:
        max_value = x

print(max_value)