tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    graph_map = {} # 그래프 맵
    # 항상 인천에서 출발한다.
    stack = ['ICN']
    answer = []
    tickets.sort(reverse=True) # 알파벳 순이 필요해서 정렬

    # 값 넣어주기
    for start, end in tickets:
        if start in graph_map:
            graph_map[start].append(end)
        else:
            graph_map[start] = [end]

    while stack:
        x = stack[-1]
        # 출발점이 없거나 도착점이 없을 때
        if x not in graph_map or len(graph_map[x]) == 0:
            answer.append(stack.pop())
        # 출발과 도착이 있을 때
        else:
            stack.append(graph_map[x].pop())

    # 출발순서는 반대
    answer.reverse()
    return answer

print(solution(tickets))