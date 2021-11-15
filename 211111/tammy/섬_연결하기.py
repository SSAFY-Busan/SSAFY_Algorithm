def solution(n, costs):
    
    visited = [0]
    tot_cost = [987654321] * n # 섬의 갯수 n개 만큼
    visited[costs[0][0]] = 1

    tot_cost[costs[0][0]] = 0
    for i in range(len(costs)) :
        if not visited[costs[i][1]] : # 현재 연결된 섬에 방문하지 않았다면
            if tot_cost[costs[i][1]] > costs[i][2]  : 
                tot_cost[costs[i][1]] = costs[i][2]
                visited[costs[i][0]] = 1

    return sum(visited)

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(5,[[0,1,1],[3,4,1],[0,2,2],[1,2,5],[2,3,8]]))
