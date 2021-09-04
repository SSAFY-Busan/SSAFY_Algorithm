# N번째 큰 수
T = int(input())

for tc in range(T):
    N_list = list(map(int, input().split()))

    # 배열의 개수는 10개 고정, 3번째 큰 수 찾기
    # 뒤에서부터 큰 값을  찾아 정렬한다. 3번 실행시에 3번째 큰 수를 찾을 수 있다.

    for i in range(9, 6, -1):
        max_num = N_list[i]
        max_index = i

        for j in range(i):
            if max_num < N_list[j]:
                max_index = j  # 최대 인덱스만 저장 하기
                max_num = N_list[j]
        # for문 다 돌았을 때 최대 인덱스와 현재 인덱스랑 교환
        N_list[i], N_list[max_index] = N_list[max_index], N_list[i]  # 인덱스이므로 10-1-i

    print(N_list[7])
