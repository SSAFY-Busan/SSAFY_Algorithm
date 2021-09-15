from collections import Counter

N = int(input())
best_seller = []
for i in range(N):
    best_seller.append(input())

# # 같을 경우 사전순 정렬 때문에 sort를 해줘야함
# best_seller.sort()
# lst = Counter(best_seller)
# print(lst.most_common(1)[0][0])

dic = {}
for book in best_seller:
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

sort_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(sort_dic[0][0])