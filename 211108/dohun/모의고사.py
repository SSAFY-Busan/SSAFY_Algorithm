answers = [1,2,3,4,5]

def solution(answers):
    # 3명의 수포자의 패턴
    first_lst = [1,2,3,4,5]
    second_lst = [2,1,2,3,2,4,2,5]
    third_lst = [3,3,1,1,2,2,4,4,5,5]
    answer = [] # 정답 리스트

    # 수포자 카운트
    first_cnt, second_cnt, third_cnt = 0, 0, 0

    # 전체 문제 돌기
    for i in range(len(answers)):
        if first_lst[i % len(first_lst)] == answers[i]:
            first_cnt += 1
        if second_lst[i % len(second_lst)] == answers[i]:
            second_cnt += 1
        if third_lst[i % len(third_lst)] == answers[i]:
            third_cnt += 1

    # 가장 많이 맞춘 사람을 기준으로 비교해서 선별
    max_score = max(first_cnt, second_cnt, third_cnt)
    if max_score == first_cnt:
        answer.append(1)
    if max_score == second_cnt:
        answer.append(2)
    if max_score == third_cnt:
        answer.append(3)
    return answer

print(solution(answers))