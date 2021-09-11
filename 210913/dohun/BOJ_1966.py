T = int(input())

for tc in range(T):
    N, M = map(int, input().split()) # N은 문서개수,
    # M은 몇번째로 인쇄되었는지 궁금한 문서 큐가 몇번째로 놓여있는지

    arr = list(map(int, input().split()))
    cnt = 0

    while arr:
        top_number = max(arr)
        pop_number = arr.pop(0)
        M -= 1
        if top_number != pop_number:
            arr.append(pop_number)
            if M < 0:
                M = len(arr) -1

        else:
            cnt += 1
            if M == -1:
                print(cnt)
                break

