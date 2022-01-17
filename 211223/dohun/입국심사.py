n = 6
times = [7,10]

def solution(n, times):
    start = min(times)
    end = max(times) * n
    while start < end:
        mid = (start + end) // 2
        people = 0
        # print("여긴 지점",start, end, mid)

        for time in times:
            people += (mid // time)
            # print("사람" ,people)
            # 사람이 초과하면 탈출
            if people >= n:
                break
        # print("-------------------")

        # 값보다 크면 왼쪽범위
        if people >= n:
            end = mid
        # 아닐 경우 오른쪽 범위
        # n보다 작으면 모두 입국심사를 하지 않았다
        else:
            start = mid + 1

    return start

print(solution(n, times))