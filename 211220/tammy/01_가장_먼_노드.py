from collections import deque

def solution(n, edge):
    adj_list=[[] for _ in range(n+1)]

    for node1, node2 in edge :
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    q = deque()
    q.append(1)
    visited = [0] * (n + 1)
    visited[1] = 1

    while q :
        connected = q.popleft()
        for node in adj_list[connected]:
            if visited[node] == 0 :
                q.append(node)
                visited[node] = visited[connected]+1

    max_num = max(visited)
    answer = 0
    for cnt in visited :
        if cnt == max_num :
            answer += 1

    return answer


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))