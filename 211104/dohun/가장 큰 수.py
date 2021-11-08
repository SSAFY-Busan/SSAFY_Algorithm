numbers = [6, 10, 2]

def solution(numbers):
    # 최대크기 1000 -> 크기대로 정렬
    sort_number = sorted(numbers, key=lambda x: str(x)*4, reverse=True)

    answer = ''
    for i in range(len(sort_number)):
        answer += str(sort_number[i])

    # 테스트 케이스 찾았다!!! 0 문자열임.
    check = False
    for i in range(len(answer)):
        if answer[i] == '0':
            check = True
        else:
            break

    if check == True:
        return '0'
    else:
        return answer
    # 0이 앞으로 올수도 있으니 처리해주기
    # cnt = 0
    # for i in range(len(answer)-1):
    #     if answer[i] == '0':
    #         cnt += 1
    #     else:
    #         break
    #
    # return answer[cnt:]


solution(numbers)

##############################################

# def solution(numbers):
#     # 전부 문자열로 변환시키기
#     numbers = list(map(str, numbers))
#     # 3자리수 맞추기 위해 *3을 해서 맞춘다. 정렬은 큰 순으로
#     numbers.sort(key=lambda x: x * 3, reverse=True)
#     # 나머지 숫자 전부 합치기
#     return str(int(''.join(numbers)))
#
# print(solution(numbers))