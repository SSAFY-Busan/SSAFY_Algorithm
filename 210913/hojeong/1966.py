# 프린터 큐
T = int(input())  # 테스트케이스 수
for tc in range(T):
    N, M = map(int, input().split())  # N: 문서의 개수 M: 궁금한 문서의 위치
    q = list(map(int, input().split()))  # 문서의 중요도
    my_lst = []  # '문서 번호 + 문서 중요도' 로 이루어진 리스트
    for i in range(1, N + 1):
        my_lst.append(q[i - 1] + i * 10)  # 중요도는 1~9이므로 무조건 한자리이다. 따라서 10의 자리수에 각 문선 번호를 1부터 N번까지 설정한다.
    g = my_lst[M] // 10  # 문서 인덱스를 가지고 찾을 문서 번호를 변수에 저장
    cnt = 0  # 몇번째 인쇄되는 지 카운트 변수

    if N == 1:  # 한 개일경우 1 출력
        print(1)
    else:
        while q:
            k = q.pop(0)  # 문서중요도 리스트 에서 첫번째 팝
            s = my_lst.pop(0)  # 문서 번호도 비교하기 위해 똑같이 팝
            c = s // 10  # 문서번호는 10으로 나눈 몫
            if len(q) == 0:  # 만약 길이가 0이면 즉 마지막 출력이므로
                print(N)  # 문서 개수 출력
                break
            elif k < max(q):  # 중요도가 낮으면
                q.append(k)  # 끝에 저장
                my_lst.append(s)  # 커스텀 리스트도 똑같이 저장
            else:
                cnt += 1  # 중요도가 높거나 같을 경우 카운트 1 증가
                if c == g:  # 찾으려는 문서번호와 같을 시
                    print(cnt)  # 출력
                    break
