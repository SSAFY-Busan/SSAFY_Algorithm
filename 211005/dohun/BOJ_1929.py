def check_prime(n):
    if n <= 1:
        return False
    i = 2
    # 제곱근까지만 검색
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

M, N = map(int,input().split())
for i in range(M,N+1):
    if check_prime(i):
        print(i)