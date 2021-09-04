# def check(a,b):
#     for i in range(min(a,b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i
import math

N = int(input())

lst = [int(input()) for _ in range(N)]

diff_lst = lst[1] - lst[0]
for i in range(2, N-1):
    diff_lst = math.gcd(diff_lst, (lst[i]-lst[i-1]))

# cnt = 0
# for i in range(lst[0], lst[-1]+1, diff_lst):
#     cnt += 1

print( (max(lst)-1) // diff_lst - (N-1))