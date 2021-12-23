def solution(clothes):
    cloth_dict=dict()
    for value,key in clothes:
        if key in cloth_dict.keys() :
            cloth_dict[key] += 1
        else :
            cloth_dict[key] = 1

    # print(cloth_dict)
    answer =1
    for value in cloth_dict.values():
        answer *= (value+1)             # 각 옷 카테고리별 경우의 수 모두 곱


    return answer-1 # 모두 안입는 경우의 수 제외

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
