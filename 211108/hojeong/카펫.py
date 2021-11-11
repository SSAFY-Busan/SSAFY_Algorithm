def solution(brown, yellow):
    # 가로,세로 최소 길이는 3
    for i in range(3, brown // 2):  # 한 변을 정하고
        j = (brown + 4 - i * 2) // 2  # 나머지 변은 자동으로 정해짐
        if (i - 2) * (j - 2) == yellow:
            a = i
            b = j
            break
    ans = [b,a]
    return ans
