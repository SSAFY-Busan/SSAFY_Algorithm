N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

dic = dict()

for target in N_arr:
    if target in dic:
        dic[target] += 1
    else:
        dic[target] = 1

for target in range(M):
    if M_arr[target] in dic:
        print(dic[M_arr[target]], end=' ')
    else:
        print(0, end=' ')