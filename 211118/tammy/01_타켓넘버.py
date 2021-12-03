sub_ans =0
def my_sum(numbers,tot,idx,target):
    global sub_ans
    # print(f'total : {tot}, visited : {visited}, idx : {idx}, num : {num}')
    # if idx == len(visited) :
    if idx == len(numbers) :
        if tot == target :
            sub_ans +=1
            return
        return

    else :
        my_sum(numbers, tot + numbers[idx], idx + 1, target)
        my_sum(numbers, tot - numbers[idx], idx + 1, target)
    # for i in range(0,len(visited)):
    #     if not visited[i] :
    #         visited[i] = 1
    #         my_sum(numbers,tot+numbers[i],visited,idx+1,target)
    #         my_sum(numbers,tot-numbers[i],visited,idx+1,target)
    #         visited[i] = 0
    #         break # 이걸 해줘야 중복X


def solution(numbers, target):
    # visited = [0]*len(numbers)

    # my_sum(numbers,0, visited,0,target)
    my_sum(numbers,0,0,target)

    answer = sub_ans
    return answer



print(solution([1, 1, 1, 1, 1],3))