# 숫자 카드
N = int(input())  # 숫자 카드 개수
cards = list(map(int, input().split()))
M = int(input())
finds = map(int, input().split())

my_dic = {}
for i in cards:
    if my_dic.get(i):  # 해당 키 값이 있으면
        my_dic[i] += 1  # 1 증가
    else:
        my_dic[i] = 1  # 없으면 추가
for i in finds:
    if my_dic.get(i):  # 해당 키 있으면 value 출력
        print(my_dic[i], end=' ')
    else:  # 없으면 0출력
        print(0, end=' ')
