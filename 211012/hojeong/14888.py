# 연산자 끼워넣기
from collections import deque
from copy import deepcopy
from itertools import permutations


def cal(arr):
    global MAX
    global MIN
    # stack 으로 풀기 위해 뒤집기
    arr = deque(arr[::-1])
    nums = deque(deepcopy(nums_origin[::-1]))  # pop을 대비해서 원본을 딥카피해서 가져와서 진행

    while 1:
        if len(nums) == 1:
            temp = nums.pop()
            if temp > MAX:
                MAX = temp
            if temp < MIN:
                MIN = temp
            return

        a = nums.pop()
        b = nums.pop()
        o = arr.pop()
        if o == '+':
            c = a + b
        elif o == '-':
            c = a - b
        elif o == '*':
            c = a * b
        elif o == '//':
            if a < 0:
                a *= -1
                c = -(a // b)
            else:
                c = a // b
        nums.append(c)


# 구현해서 사용시 시간 초과

# def perm(idx):
#     if idx == N-1:
#         sel=deepcopy(operators)
#         cal(sel)
#         return
#
#     for i in range(idx, N-1):
#         operators[idx], operators[i] = operators[i], operators[idx]
#         perm(idx + 1)
#         operators[idx], operators[i] = operators[i], operators[idx]

# 입력
N = int(input())
nums_origin = list(map(int, input().split()))
temp = list(map(int, input().split()))

# 입력 받은 연산자 풀어서 나열
operator = ['+', '-', '*', '//']
operators = []
for i in range(4):
    if temp[i]:
        for j in range(temp[i]):
            operators.append(operator[i])

# 순열 구해서 계산하기
MIN = 999999999
MAX = -999999999
permutation = set(permutations(operators))
for k in permutation:
    cal(k)

# 출력
print(MAX)
print(MIN)
