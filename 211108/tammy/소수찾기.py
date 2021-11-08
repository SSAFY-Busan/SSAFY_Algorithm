from itertools import permutations

def solution(numbers):

    permu = set()
    for i in range(1, len(numbers)+1): 
        ls = list(permutations(numbers,i)) # 1자리부터 len(numbers)자리까지 조합
        for j in range(len(ls)) :
            permu.add(int(''.join(ls[j]))) # str형태로 묶어서 add

    answer = 0
    permu = list(permu) # iterable하게 바꿔줌

    for i in range(len(permu)):
        flag = 0
        if permu[i] > 1:
            num = 2 # 소수는 only 1과 자기자신만을 약수로 가지므로 2부터 나눠봄
            while num <= permu[i]**(1/2): # 에라스토테네스의 체
                if permu[i] % num == 0: # 2이상의 수에서 딱떨어진다면 소수 탈락
                    # print(permu[i], num)
                    flag = 1
                    break
                num += 1
            if flag == 0 :
                answer += 1


    
    return answer



print(solution("17"))