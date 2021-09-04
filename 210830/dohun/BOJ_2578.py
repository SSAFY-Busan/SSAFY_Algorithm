def check(visited):
    cnt = 0
    # 가로체크
    for i in range(5):
        if sum(visited[i][:]) == 5:
            cnt += 1

    for i in range(5):
        sum_check = 0
        for j in range(5):
            sum_check += visited[j][i]
        if sum_check == 5:
            cnt += 1

    cnt_num = 0
    for i in range(5):
        cnt_num += visited[i][i]
        if cnt_num == 5:
            cnt += 1

    cnt_num = 0
    for i in range(5):
        cnt_num += visited[i][4-i]
        if cnt_num == 5:
            cnt += 1

    return cnt

graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]

lst = []
for _ in range(5):
    x = list(map(int, input().split()))
    for i in x:
        lst.append(i)

check_test = False
idx = 0
for k in lst:
    idx += 1
    for i in range(5):
        for j in range(5):
            if graph[i][j] == k:
                visited[i][j] = 1
                if check(visited) >= 3:
                    check_test = True
                    break
        if check_test == True:
            break
    if check_test == True:
        break

print(idx)