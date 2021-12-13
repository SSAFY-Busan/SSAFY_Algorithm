from collections import deque
from copy import deepcopy


def solution(tickets):
    tickets.sort(key=lambda x: x[1])  # 오름차순 정렬

    def bfs():
        q = deque()
        l = len(tickets)
        q.append(("ICN", ["ICN"], [0 for _ in range(l)]))  # 출발지, 경로, 방문
        while q:
            dst, route, visited = q.popleft()
            if len(route) == l + 1:  # 경로가 티켓길이 +1 이면 경로 반환
                return route
            for i in range(l):
                if tickets[i][0] == dst and not visited[i]:  # 출발지가 같고 방문하지 않았으면
                    visited[i] = 1  # 방문체크
                    newvisited = deepcopy(visited)
                    q.append((tickets[i][1], route + [tickets[i][1]], newvisited))
                    visited[i] = 0  # 방문해제

    answer = bfs()
    return answer

