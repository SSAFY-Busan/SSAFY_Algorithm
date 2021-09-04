T = int(input()) # 테스트 케이스

for tc in range(T):
    N = int(input())
    cnt = 0
    arr_a = input()
    arr_b = input()
    answer = []
    result = 0

    for i in range(N):
        if arr_a[i] != arr_b[i]:
            answer.append(arr_a[i])

    if answer.count('W') >= answer.count('B'):
        result = answer.count('W')
    else:
        result = answer.count('B')

    print(result)