def solution(n, times):
    # 테케 4~9 시간 초과
    # origin_times = times[:]
    # time_list =[]
    #
    # while len(time_list) != n :
    #     idx, time = min(enumerate(times), key= lambda x : x[1])
    #     time_list.append(time)
    #     times[idx] += origin_times[idx]
    #
    # return time_list[-1]
    origin_times = times[:]
    time_list = []
    count =0
    while count != n :
        for i in range(len(times)) :
            time_list.append(times[i])
            times[i] += origin_times[i]

        count += 1
    time_list.sort()
    return time_list[n-1]
print(solution(6, [7,10]))
