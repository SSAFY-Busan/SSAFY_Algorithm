import math
from itertools import permutations

# 소수 판별
def is_prime(num):
    # 1이나 0일 경우 소수이므로 False
    if num == 0 or num == 1:
        return False
    else:
        # 소수를 발견하면 그대로 종료
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        num_lst = list(permutations(numbers, i))

        for num in num_lst:
            x = int(''.join(num))
            if is_prime(x):
                answer.append(x)

    # 중복제거 -> 두번째 케이스 같은경우 중복이 일어남
    answer = list(set(answer))
    return len(answer)

numbers = "011"
print(solution(numbers))