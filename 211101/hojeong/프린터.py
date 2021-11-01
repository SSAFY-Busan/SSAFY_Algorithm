def solution(priorities, location):
    answer = 0
    while 1:
        MAX = max(priorities)
        temp = priorities.pop(0)
        if temp >= MAX:  # 해당 값이 우선순위가 가장 클 때
            answer += 1  # 인쇄
            if location == 0:  # 찾는 인덱스면 멈춤
                break
            else:
                location -= 1  # 아니면 -1 (왼쪽으로 이동)
        else:  # 우선순위가 최대가 아닐 때
            priorities.append(temp)  # 마지막에 넣기
            if location:  # location이 0이 아니라면
                location -= 1
            else:  # 0이라면
                location = len(priorities) - 1  # 마지막 인덱스로

    return answer
