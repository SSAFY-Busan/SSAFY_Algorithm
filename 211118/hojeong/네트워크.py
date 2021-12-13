def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]:  # 연결되어있고 방문하지 않은곳이면
                dfs(j)

    for i in range(n):
        if not visited[i]:  # 방문하지 않은 곳이라면
            dfs(i)
            answer += 1
    return answer
