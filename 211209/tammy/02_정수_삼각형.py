# 시간 초과
# from collections import deque
# max_value = 0
# def bfs(triangle) :
#     global max_value
#     q = deque()
#     q.append((triangle[0][0],0,0))
#     while q :
#         sub_sum , depth, idx = q.popleft()
#
#         if depth == len(triangle)-1 :
#             if max_value < sub_sum :
#                 max_value = sub_sum
#         else :
#             q.append((sub_sum+triangle[depth+1][idx], depth+1, idx))
#             q.append((sub_sum+triangle[depth+1][idx+1], depth+1, idx+1))




def solution(triangle):
    # global max_value
    # bfs(triangle)

    for i in range(1, len(triangle)) :
        for j in range(len(triangle[i])):
            if j == 0 : # 양끝값은 더해지
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1 :
                triangle[i][j] += triangle[i - 1][j-1]
            elif triangle[i-1][j-1] > triangle[i-1][j] :
                triangle[i][j] += triangle[i-1][j-1]
            else :
                triangle[i][j] += triangle[i - 1][j]

    answer = max(triangle[len(triangle)-1])



    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))