answer=0
def solution(numbers, target):
    n=len(numbers) # 숫자 개수
    def dfs(idx,temp):
        global answer
        if idx==n: # 개수 다 계산했으면
            if temp==target: # 타겟 숫자랑 같은지 비교
                answer+=1
            return
        else:
            dfs(idx+1,temp+numbers[idx]) # 더하기
            dfs(idx+1,temp-numbers[idx]) # 빼기
    dfs(0,0)
    return answer
# def solution(numbers, target):
#     global answer
#     dfs(0,0,numbers,target)
#     return answer
# def dfs(idx,temp,numbers,target):
#     global answer
#     n = len(numbers)  # 숫자 개수
#     if idx==n:
#         if temp==target:
#             answer+=1
#         return
#     else:
#         dfs(idx+1,temp+numbers[idx],numbers,target)
#         dfs(idx+1,temp-numbers[idx],numbers,target)
#
# answer=0
# numbers=[1,1,1,1,1]
# target=3
# print(solution(numbers,target))
