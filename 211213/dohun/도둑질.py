money = [1,2,3,1]

def solution(money):
    money_length = len(money) # 돈 길이

    step1 = [money[0], money[0]]
    step2 = [0, money[1]]

    # 0번째 시작
    for i in range(2, money_length-1):
        step1.append(max(step1[i-2] + money[i], step1[i-1]))

    # 첫번째 시작작
    for i in range(2, money_length):
        step2.append(max(step2[i-2] + money[i], step2[i-1]))

    # print(step1)
    # print(step2)
    answer = max(step1[-1], step2[-1])
    return answer

print(solution(money))