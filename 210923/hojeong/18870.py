# 좌표 압축
import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
custom_lst = list(set(lst))  # 중복 제거
custom_lst.sort()  # 오름차순 정렬
my_dict = {}
for i in range(len(custom_lst)):
    my_dict[custom_lst[i]] = i  # 오름차순으로 정렬했기 때문에 나보다 작은 개수는 인덱스와 같다
for i in lst:
    print(my_dict[i], end=' ')
