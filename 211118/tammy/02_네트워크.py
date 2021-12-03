def dfs(curr,adj_list,visited) :
    visited[curr] = 1

    for i in adj_list[curr]:
        if not visited[i] :
            dfs(i,adj_list,visited)

    return visited





def solution(n, computers):
    visited =[0] * n
    adj_list = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j] == 1 :
                adj_list[i].append(j)
    print(adj_list)

    cnt =0
    for i in range(n):
        if not visited[i] :
            visited = dfs(i,adj_list,visited)
            cnt+=1
    return cnt

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))