N = int(input())
lst = []
for _ in range(N):
    a, b = map(str, input().split())
    lst.append((int(a),b))

sort_lst = sorted(lst, key=lambda x:x[0])

for i in sort_lst:
    print(i[0], i[1])