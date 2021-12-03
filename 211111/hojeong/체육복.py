def solution(n, lost, reserve):
    ans = 0
    # 학생 수 크기 리스트
    check = [1] * n

    # 도난 학생 -1
    for i in lost:
        check[i - 1] -= 1
    # 여벌 학생 +1
    for i in reserve:
        check[i - 1] += 1

    # 빌려주기
    # 앞 확인-> 뒤 확인
    for i in range(n):
        if check[i] == 0:
            if i - 1 >= 0 and check[i - 1] == 2:
                check[i] = 1
                check[i - 1] = 1
            elif i + 1 < n and check[i + 1] == 2:
                check[i] = 1
                check[i + 1] = 1

    # 체육수업 들을 수 있는 학생 카운트
    for i in check:
        if i:
            ans += 1
    return ans
