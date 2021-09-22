N = int(input())

for i in range(2, N+1):
    # 끝에 도달하면 그냥 출력
    if N == i:
        print(i)
        break

    while N % i == 0:
        print(i)
        N //= i