def solution(money):
    # check = [False]*len(money)
    #
    # total = 0
    # for i in range(len(money)-1) :
    #     if not check[i-1] and money[i] >= money[i-1] : # 앞에 체크 없고 그 전 값보다 크다면
    #         total += money[i]
    #         check[i] = True
    #     elif check[i-1] and money[i] >= money[i-1] and money[i] >= money[i+1]:
    #         total -= money[i-1]
    #         check[i-1] = False
    #         check[i]=True
    #         total += money[i]
        # print(check)
    # 경우의 수 는 두가지로 나온다.
    # 1.  첫번째 집을 턴 경우
    # 2. 첫 번째 집을 털지 않은 경우
    # 3. 그 안에서, 그 전까지의 값과, 그 전전집과 현재 집을 털었을 때의 max 값


    get_money = [money[0], money[0]] # 첫번째 집 털기
    get_money2 = [0, money[1]] # 첫 번째 집 털지않기

    for i in range(2, len(money)-1):
        get_money.append(max(get_money[i-1], get_money[i-2]+money[i]))

    for i in range(2, len(money)-1):
        get_money2.append(max(get_money2[i-1], get_money2[i-2]+money[i]))

    return max(get_money[-1], get_money2[-1])

print(solution([1,2,3,1])) # 4
print(solution([1,1,4,1,4])) # 8
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000) # 3000
print(solution([1000,1,0,1,2,1000,0])) # 2001
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000])) #2000
print(solution([1,2,3,4,5,6,7,8,9,10])) # 30
print(solution([0,0,0,0,100,0,0,100,0,0,1,1])) # 201
print(solution([11,0,2,5,100,100,85,1])) # 198
print(solution([1,2,3])) # 3
print(solution([91,90,5,7,5,7])) # 104
print(solution([90,0,0,95,1,1])) # 185