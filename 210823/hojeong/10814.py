#나이순 정렬
N=int(input())
lst=[]
for i in range(N):
    a,n=input().split()
    lst.append((int(a),n))

sort_lst=sorted(lst,key=lambda x:x[0])

for i in sort_lst:
    print(i[0], i[1])
# import operator
#폐기...
# N=int(input())
# my_dic={}
# for i in range(N):
#     a,n=input().split()
#     my_dic[n]=int(a)
# result=sorted(my_dic.items(),key=lambda x:x[1]) # key=operator.itemgetter(1)
# for i in range(N):
#     print('{} {}'.format(result[i][1],result[i][0]))






