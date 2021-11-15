def solution(name):

    #알파벳 바꾸기
    change_word = 0
    cnt =[0]*len(name)                          # 위치바꿀때 바꿨는지 세어주기 위한 리스트(바꿔야하는 경우 0, 바꿀필요 없는 경우 1)
    cnt[0]=1                                    # 맨처음은 위치 바꿀 필요 없으므로 1
    for i in range(len(name)) :
        if name[i] == 'A':
            cnt[i] = 1                           # A인 경우 알파벳 바꿀 필요 없으므로 1 로 체크
        change_word += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1) #A = 65, Z=90 / 초기값 A로 잡혀있으므로 Z에서 현재 알파벳 뺄땐 +1

    # 위치
    idx = 0 # 현재위치
    change_loca = 0 # 바꿔준 위치 누적합 해줄 변수
    while True:
        if sum(cnt) == len(name): # 알파벳 모두 바꿨는지 체크
            break
        left = idx-1    # 현재위치에서 왼쪽으로 갈 변수
        right = idx+1   # 현재위치에서 오른쪽으로 갈 변수
        cnt_l = 1       # 왼쪽으로 몇 번 가야하는지 세어줄 cnt 변수
        cnt_r = 1       # 오른쪽으로 몇 번 가야하는지 세어줄 cnt 변수
        while cnt[right] != 0:  # 오른쪽으로 이동
            right +=1
            cnt_r +=1
        while cnt[left] != 0:   # 왼쪽으로 이동
            if left == -1 :     # - 인덱스일경우 양수인덱스로 변환
                left = len(name)-1
            left -=1
            cnt_l +=1

        if cnt_r <= cnt_l :     # 일단 오른쪽으로 가는걸 우선시 할 것이므로 =도 붙여줘야함./ 오른쪽 cnt가 더 적은경우
            change_loca += cnt_r# 누적합
            idx = right         # 현재위치 바꿔주기
            cnt[idx] = 1        # cnt리스트에 체크
        else :                  # 왼쪽 cnt가 더 적은경우
            change_loca += cnt_l
            idx = left
            cnt[idx] = 1



    return change_word + change_loca

print(solution('JEROEN'))
print(solution('JAN'))
print(solution('AAAA'))