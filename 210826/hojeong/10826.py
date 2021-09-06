# 피보나치 수4
def my_fibo(N):
    if N <= 1:
        return N
    else:
        return my_fibo(N - 1) + my_fibo(N - 2)


def my_fibo2(N):
    if N==1:
        return 1
    a = 0
    b = 1
    ans = 0
    for i in range(N - 1):
        ans = a + b
        a, b = b, ans
    return ans


n = int(input())
print(my_fibo2(n))
