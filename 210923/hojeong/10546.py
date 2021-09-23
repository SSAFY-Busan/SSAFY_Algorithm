# 배부른 마라토너
import sys

N = int(input())  # 참가자 수
name = {}  # 참가자 명단 딕셔너리 동명이인 체크
for i in range(N):
    temp = sys.stdin.readline()
    if temp in name:
        name[temp] += 1
    else:
        name[temp] = 1
for i in range(N - 1):
    name[sys.stdin.readline()] -= 1

for i in name:
    if name[i] == 1:
        print(i)
        break
