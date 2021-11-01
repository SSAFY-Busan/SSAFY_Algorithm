# 로또
from itertools import combinations
while 1:
    temp=list(map(int,input().split()))
    k=temp.pop(0)
    if k==0:
        break
    else:
        combination=combinations(temp,6)
        for i in combination:
            print(*i)
    print()

