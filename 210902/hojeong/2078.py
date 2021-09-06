# 무한이진트리
import sys
L,R=map(int,sys.stdin.readline().split())
l_cnt=0
r_cnt=0
while 1:
    if L==1 and R==1:
        break
    if L==1:
        r_cnt+=R-1
        break
    if R==1:
        l_cnt+=L-1
        break
    if L>R:
        L=L-R
        l_cnt+=1
    if L<R:
        R=R-L
        r_cnt+=1
print(l_cnt,r_cnt)
