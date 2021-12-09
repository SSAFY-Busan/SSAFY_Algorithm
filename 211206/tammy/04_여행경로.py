global_tickets =[]
answer =[]
flag =0
def dfs(cnt,visited) :
    global answer, flag

    if sum(visited) == len(visited) :
        flag = 1
        return answer
    for i in range(len(global_tickets)) :
        if not visited[i] and answer[-1] == global_tickets[i][0] :
            # print(visited,answer)
            visited[i] = 1
            answer.append(global_tickets[i][1])
            dfs(cnt+1,visited)
            visited[i] = 0

            if flag :
                return
            answer.pop()







def solution(tickets):
    global global_tickets, answer
    tickets.sort(key=lambda x : x[1]) # 알파벳 빠른순으로 가기 위해
    print(tickets)
    global_tickets = tickets
    visited = [0] * len(tickets)
    for i in range(len(tickets)) :
        if tickets[i][0] == 'ICN' : # 출발지가 인천이면
            visited[i] = 1
            answer = tickets[i]
            dfs(1,visited)
            visited[i] = 0
            if len(answer) == len(tickets)+1 :
                return answer


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))
# print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))
# tickets=[["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]] # ["ICN", "B", "ICN", "A", "D", "A"]