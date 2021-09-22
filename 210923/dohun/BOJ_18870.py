N = int(input())

arr = list(map(int, input().split()))
sort_arr = list(sorted(set(arr)))
# lst = [[sort_arr[i], i] for i in range(len(sort_arr))]
dic = {sort_arr[i]:i for i in range(len(sort_arr))}

for i in arr:
    print(dic[i], end=' ')