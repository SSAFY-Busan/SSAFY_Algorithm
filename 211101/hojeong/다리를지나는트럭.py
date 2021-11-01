def solution(bridge_length, weight, truck_weights):
    answer = 0  # 총 시간
    cur = [0] * bridge_length  # 다리를 건너는 트럭
    while len(cur) != 0:
        cur.pop(0)
        answer += 1
        if truck_weights:  # 대기 트럭이 있다면
            if sum(cur) + truck_weights[0] <= weight:  # 무게가 넘지 않으면
                cur.append(truck_weights.pop(0))  # 맨 앞 대기 트럭 출발
            else:
                cur.append(0)  # 무게가 넘으면 0 추가 (빈값)
    return answer
