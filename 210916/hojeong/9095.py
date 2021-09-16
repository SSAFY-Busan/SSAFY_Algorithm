# 1,2,3더하기
# top-down
def my_fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return my_fun(n - 1) + my_fun(n - 2) + my_fun(n - 3)


T = int(input())  # 테스트케이스 수
for tc in range(T):
    print(my_fun(int(input())))
