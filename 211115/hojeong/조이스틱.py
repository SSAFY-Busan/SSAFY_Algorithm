def solution(name):
    # 알파벳 길이만큼 체크리스트 -> 초기값 Fasle
    check = [False] * len(name)
    # 이미 'A'인건 True로 바꿔주기
    for i in range(len(name)):
        if name[i] == 'A':
            check[i] = True

    # 검사하는 알파벳 인덱스
    idx = 0
    # 조작 횟수
    cnt = 0
    # 방향 (1:오른쪽,-1:왼쪽)
    d = 1

    while 1:
        # 'A'가 아니라면 X-'A'와 'Z'-X+1 중 최소값
        if check[idx] == False:
            temp = abs(ord('A') - ord(name[idx]))
            cnt += min(temp, 26 - temp)
            check[idx] = True

        # 탈출 조건->모두 검사
        if sum(check) == len(name):
            break

        # 방향 탐색
        l = 1
        flag = False
        while 1:
            for i in [1, -1]:
                t = i * l
                if check[idx + t] == False:
                    d = i
                    flag = True
                    break
            if flag:
                break
            l += 1
        idx += d
        cnt += 1
    return cnt