import sys
N = int(input())

input = sys.stdin.readline

lst = []
for _ in range(N):
    # 입력받아서 리스트에 추가
    a, b = map(int, input().split())
    lst.append((a,b))

# 정렬 앞에꺼 먼저 정렬, 뒤에꺼 정렬
lst.sort(key=lambda x:(x[0], x[1]))
for x in lst:
    print(x[0],x[1])