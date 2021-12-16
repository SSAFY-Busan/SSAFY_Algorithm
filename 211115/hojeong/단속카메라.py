def solution(routes):
    answer,end=0,-30001
    routes.sort(key=lambda x:x[1])
    for route in routes:
        if end<route[0]:
            end=route[1]
            answer+=1
    return answer