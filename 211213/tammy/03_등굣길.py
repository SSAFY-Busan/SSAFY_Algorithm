def solution(m, n, puddles):

    my_map = [[1]*m for _ in range(n)]

    for _ in range(len(puddles)):
        if puddles[_][1]-1 == 0 : # 행
            for k in range(puddles[_][0]-1,m):
                my_map[0][k] = 0
        elif puddles[_][0]-1 == 0 :
            for k in range(puddles[_][1]-1,n):
                my_map[k][0] = 0
        else:
            my_map[puddles[_][1]-1][puddles[_][0]-1] = 0 # puddle 열, 행으로 있다
    for i in range(1,n):
        for j in range(1,m):
            if my_map[i][j] == 0 :
                continue
            else :
                my_map[i][j] = my_map[i][j-1] + my_map[i-1][j]

    # for k in range(n):
    #     print(*my_map[k])
    return my_map[n-1][m-1] % 1000000007

print(solution(4,3,[[2,2],[2,1],[1,2]]))