# 평균

#최대값 찾는 함수
def myMax(lst):
    num = lst[0]
    for i in lst:
        if num < i:
            num = i
    return num

#누적합 구하는 함수
def mySum(lst):
    total = 0
    for i in lst:
        total += i
    return total


N = int(input()) #과목 수
score = list(map(int, input().split())) # 각 점수
M = myMax(score) #최대 점수
for i in range(len(score)): # 갱신
    score[i] = score[i] / M * 100
print(mySum(score) / N) #평균 출력
