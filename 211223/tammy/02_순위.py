# 어거지로 풀긴 품..
# 플로이드 와샬 알고리즘 이용해서 풀어보기
def solution(n, results):
    answer = 0
    adj_arr = [[] for _ in range(n+1)]
    for_check_list = [[] for _ in range(n+1)]
    # 전적 기록
    for node1, node2 in results :
        adj_arr[node1].append((node2,'win'))
        adj_arr[node2].append((node1,'lose'))

        for_check_list[node1].append(node2)
        for_check_list[node2].append(node1)
    # print(adj_arr)
    # print(for_check_list)
    # 아이디어
    # 내가 A한테 이겼다면 A 한테 진 애들한테도 이긴 것
    # 내가 B한테 졌다면 B를 이긴 사람한테도 진 것
    count = 0
    while count !=2:
        for i in range(1,n+1) : # 나
            if len(adj_arr[i]) != n-1 : # 모든 사람과 승부를 겨룬 사람은 순위가 정해졌으므로 할 필요 없음

                for j in range(len(adj_arr[i])) : # 내가 겨뤄본 사람

                    person, win_or_lose = adj_arr[i][j][0], adj_arr[i][j][1] # 내가 겨룬 사람, 승/패 전적

                    # print(f'나 : {i} ,내가 겨룬 사람 :{person}, 전적 : {win_or_lose}')

                    for p, w_o_l in adj_arr[person]: # 겨뤄본 사람이 겨룬 사람과 전적
                        if win_or_lose == 'win' : # 내가 이겼다면 p한테 진 사람한테도 이긴 것을 기록
                            if p != i and p not in for_check_list[i] and w_o_l=='win' : # 중복되지 않게 하기위한 조건 + 내가 이긴사람한테 진사람이라면
                                adj_arr[i].append((p,'win'))
                                for_check_list[i].append(p)
                        else :
                            # print(f'나 : {i} ,내가 겨룬 사람의 idx :{p}, 전적 : {w_o_l}')
                            if p != i and p not in for_check_list[i] and w_o_l == 'lose':  # 중복되지 않게 하기위한 조건 + 내가 진사람한테 이긴사람이라면
                                adj_arr[i].append((p, 'lose'))
                                for_check_list[i].append(p)
        count += 1
    # print(adj_arr)
    # print(for_check_list)
    for i in range(len(for_check_list)) :
        if len(for_check_list[i]) == n-1 :
            answer += 1
    # print(for_check_list)

    return answer



# print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(4, [[1,2],[2,3],[1,4]]))
print(solution(5 ,[[1, 2], [4, 5], [3, 4], [2, 3]]))