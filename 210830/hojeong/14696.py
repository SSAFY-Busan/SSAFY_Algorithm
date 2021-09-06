# 딱지놀이

# 우선순위
# 별 - 동그라미- 네모-세모
N = int(input())  # 라운드 수
for i in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    a = A.pop(0)  # A의 길이
    b = B.pop(0)  # B의 길이

    A.sort(reverse=True)  # 내림차순 정렬
    B.sort(reverse=True)
    # 길이 같게 만들기
    while a != b:
        if a > b:
            B.append(0)
            b += 1
        elif a < b:
            A.append(0)
            a += 1

    for j in range(a):
        if A[j] > B[j]:
            print('A')
            break
        elif A[j] < B[j]:
            print('B')
            break
    else:
        print('D')
