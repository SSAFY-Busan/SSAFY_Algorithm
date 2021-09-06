def hanoi(n,a,b,c):
    # print(n,a,b,c)
    if n == 0:
        return
    else:
        # print("n은",n)
        hanoi(n-1, a, c, b) # 하나 적은 원반들을 목적지가 아닌곳으로 이동
        print(a, c) # 맨 아래 원반을 목적지로 이동
        # print("n은",n)
        hanoi(n-1, b, a, c) # 마지막을 다른곳으로 옮겼던 원판을 얹는다.

n = int(input())
sum = 1
for i in range(n-1):
    sum = sum * 2 + 1
print(sum)
hanoi(n,1,2,3)