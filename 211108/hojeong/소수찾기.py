from itertools import permutations


def solution(numbers):
    # 소수 담을 변수(중복x)
    nums = set()

    # 조합
    for n in range(len(numbers)):
        # n+1개 만큼 뽑기
        permutation = set(permutations(numbers, n + 1))
        # 문자열-> 숫자 -> 소수 판별
        for i in permutation:
            temp = ''.join(i)
            temp = int(temp)
            if temp < 2:
                continue
            else:
                for j in range(2, int(temp**(1/2))+1): # 에라토스테네스의 체
                    if temp % j == 0:
                        break
                else:
                    nums.add(temp)
    return len(nums)