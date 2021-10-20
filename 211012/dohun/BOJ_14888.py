def DFS(cnt, result, plus, minus, mul, div):
    global min_value, max_value
    if cnt == N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if plus > 0:
        DFS(cnt+1, result + arr[cnt], plus-1, minus, mul, div)
    if minus > 0:
        DFS(cnt+1, result - arr[cnt], plus, minus-1, mul, div)
    if mul > 0:
        DFS(cnt+1, result * arr[cnt], plus, minus, mul-1, div)
    if div > 0:
        # 음수인 경우
        if result < 0:
            DFS(cnt + 1, -(-result // arr[cnt]), plus, minus, mul, div - 1)
        else:
            DFS(cnt+1, result // arr[cnt], plus, minus, mul, div-1)

N = int(input())

arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_value = 1000000000
max_value = -1000000000

DFS(1, arr[0], plus, minus, mul, div)

print(max_value)
print(min_value)