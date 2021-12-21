from collections import deque

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    # print(graph)

    # 출발노드 1
    queue = deque([1])
    distance[1] = 0

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            # 가보지 않은 곳이면
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1

    # print(distance)

    # 가장 먼곳 몇개인지 찾기
    for dis in distance:
        if dis == max(distance):
            answer += 1

    return answer

print(solution(n, edge))