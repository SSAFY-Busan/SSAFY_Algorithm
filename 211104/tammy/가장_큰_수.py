def solution(numbers):
    numbers = [[numbers[i],(str(numbers[i])*4)[0:4]] for i in range(len(numbers))]
    # print(numbers)

    numbers.sort(key=lambda x : x[1], reverse=True)
    # print(numbers)
    answer = ''

    for i in range(len(numbers)) :
        answer += str(numbers[i][0])
    if answer[0] =='0':
        return '0'
    return answer


print(solution([3, 30, 34, 5, 9]))
print(solution([6,5,56,53,4,3,2,1]))
print(solution([98,9808]))
print(solution([0,0,0,0]))