def solution(answers):
    # 최대 10000문제이므로, 최대문제길이만큼 만들어 준다.
    person1 = [1,2,3,4,5] * 2000
    person2 = [2,1,2,3,2,4,2,5] * 1250
    person3 = [3,3,1,1,2,2,4,4,5,5] * 1000

    # 맞을때 마다, 카운트올리기
    cnt=[0,0,0]

    for i in range(len(answers)):
        if answers[i] == person1[i]:
            cnt[0] += 1
        if answers[i] == person2[i]:
            cnt[1] += 1
        if answers[i] == person3[i]:
            cnt[2] += 1

    max_cnt = max(cnt)
    answer = []
    for i in range(3):
        if max_cnt == cnt[i] :
            answer.append(i+1)


    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))