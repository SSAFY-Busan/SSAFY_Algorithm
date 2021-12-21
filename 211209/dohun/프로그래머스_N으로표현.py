N, number = 5, 12

def solution(N, number):
    # N이랑 number가 같다면 1회 출력
    if N == number:
        return 1
    answer = -1

    # 최대값이 8개다
    total_lst = [set() for i in range(8)]
    for i in range(8):
        total_lst[i].add(int(str(N)*(i+1)))

    # print(total_lst)
    for i in range(8):
        for j in range((i+1)//2):
            # 나눌수 있는 경우의 수
            for a in total_lst[i-j-1]:
                for b in total_lst[j]:
                    total_lst[i].add(a + b)
                    total_lst[i].add(a - b)
                    total_lst[i].add(a * b)
                    total_lst[i].add(b - a)
                    if a != 0:
                        total_lst[i].add(b//a)
                    if b != 0:
                        total_lst[i].add(a//b)

    # print(total_lst)
    # 앞에 인덱스에 있으면 그냥 그대로 반환
    for i in range(8):
        # print(i)
        if number in total_lst[i]:
            return i + 1

    return answer

print(solution(N, number))