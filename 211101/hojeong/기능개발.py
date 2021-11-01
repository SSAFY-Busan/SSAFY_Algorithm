def solution(progresses, speeds):
    answer = []
    day=0 # 처리 소요 시간
    cnt=0 # 배포할 수 있는 기능
    while len(progresses)!=0:
        if progresses[0]+day*speeds[0]>=100: # 처리 완료
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        else:
            if cnt: # 배포 가능한 기능이 있다면
                answer.append(cnt)
                cnt=0 #초기화
            else:
                day+=1 # 1일 증가

    if cnt: # 남아있는 거 출력
        answer.append(cnt)
    return answer