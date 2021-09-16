# 베스트셀러
import collections

N = int(input())  # 책의 개수
sell = [input() for i in range(N)]  # 책리스트
my_dic = collections.Counter(sell)  # {책:개수} 딕셔너리

# my_dic={}
# for i in range(N):
#     s=input()
#     if my_dic.get(s):
#         my_dic[s]+=1
#     else:
#         my_dic[s]=1

max_cnt = max(my_dic.values())  # 최대 개수
book = []  # 가장많이 팔린 책 리스트
for i in my_dic.keys():
    if my_dic[i] == max_cnt:
        book.append(i)
book.sort()  # 사전순으로 정렬

print(book[0])
