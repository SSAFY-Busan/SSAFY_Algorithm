# 로프
# def myMin(lst):
#     num=lst[0]
#     num_index=0
#     sorted_lst=[]
#     N=len(lst)
#     while lst:
#         for i in range(N):
#             if num>lst[i]:
#                 num=lst[i]
#                 num_index=i
#         sorted_lst.append(lst.pop(num_index))
#     return sorted_lst
#
# def mySort(lst):
#     N=len(lst)
#     for i in range(N-1):
#         max_index = i
#         for j in range(i+1,N-1-i):
#             if lst[max_index]<lst[j]:
#                 max_index=j
#         lst[i],lst[max_index]=lst[max_index],lst[i]
#     return lst



N = int(input())  # 로프 줄 수
W = []
for i in range(N):
    W.append(int(input()))
W.sort()
max_w = 0  # 최대중량
cnt = N  # 로프 개수
# W=mySort(W)

# 로프*로프가 들 수 있는 최대 중량= 총 들어올릴수 있는 중량
# 중량 작은 거 부터 확인
for i in W:
    if max_w < i * cnt:
        max_w = i * cnt
    cnt -= 1
print(max_w)
