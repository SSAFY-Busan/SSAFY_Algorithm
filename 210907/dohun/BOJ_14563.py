N = int(input()) # N 입력받기

arr = list(map(int, input().split())) # 리스트로 숫자 입력받기
for num in arr:
    lst = [] # 약수 입력받을 리스트
    for i in range(1, num//2 + 1): # 2가 나눌수 있는 제일 마지막 수이므로 2로 나눈수까지만 확인한다.
        if num % i == 0: # 나누어지면 약수이므로 리스트에 추가
            lst.append(i)

    if sum(lst) == num:
        print("Perfect")
    elif sum(lst) > num:
        print("Abundant")
    else:
        print("Deficient")