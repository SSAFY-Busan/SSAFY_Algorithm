# 수 찾기
# 이분탐색
def my_search(st, ed, n):  # st:시작 인덱스 ed: 끝 인덱스 n:찾는 숫자
    if st > ed:
        return 0
    mid = (st + ed) // 2  # mid: 중간 인덱스
    middle = n_lst[mid]  # middle: 중간 값
    if n == middle:
        return 1
    elif n < middle:
        return my_search(st, mid - 1, n)
    else:
        return my_search(mid + 1, ed, n)


N = int(input())
n_lst = sorted(list(map(int, input().split())))
M = int(input())
m_lst = map(int, input().split())

for i in m_lst:
    print(my_search(0, N - 1, i))
