#통계학
import sys

N=int(input())
nums=[0]*N
for i in range(N):
    nums[i]=int(sys.stdin.readline())
my_num=sorted(nums)
avg=sum(nums)/N
middle=my_num[N//2]
cnt={}
for i in my_num:
    try:
        cnt[i]+=1
    except:
        cnt[i]=1
sort_cnt=sorted(cnt.items(),key=lambda x:x[1],reverse=True)
if N==1:
    most=sort_cnt[0][0]
elif sort_cnt[0][1]!=sort_cnt[1][1]:
    most=sort_cnt[0][0]
else:
    most=sort_cnt[1][0]
ra=my_num[-1]-my_num[0]
print('{0}'.format(round(avg)))
print(middle)
print(most)
print(ra)