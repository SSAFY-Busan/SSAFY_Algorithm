clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    dic = {}
    for name, model in clothes:
        # print(name, model)
        dic[model] = dic.get(model, 0) + 1
        # if model not in dic:
        #     dic[model] = 1
        # else:
        #     dic[model] += 1


    print(dic)
    answer = 1
    # 착용안하는경우 생각해서 원래것보다 + 1해서 곱하기
    for cnt in dic.values():
        answer *= (cnt + 1)

    # 모두 착용안하는경우가 카운트 되기 때문에 -1 해준다.
    return answer - 1

print(solution(clothes))