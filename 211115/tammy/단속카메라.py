def solution(routes):
    routes.sort(key=lambda x: x[1]) # 나간 지점 기준으로 sort

    camera_cnt = 0                  # 카메라 갯수
    camera_location = -30001        # 카메라 위치

    for i in range(len(routes)):
        if camera_location < routes[i][0]:      # 카메라 위치가 진입지점보다 작다면
            camera_location = routes[i][1]      # 진출지점에 카메라를 두고
            camera_cnt +=1                       # 카메라 갯수 +1
        elif camera_location >= routes[i][0] :  # 그렇지 않다면 넘어가기
            continue

    return camera_cnt




print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
