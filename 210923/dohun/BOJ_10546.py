import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
dic = {}

while True:
    if cnt == N*2-1:
        break

    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
    cnt += 1

for key, value in dic.items():
    if value % 2 == 1:
        print(key)
        break