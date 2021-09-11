# from collections import deque
#
# N = int(input())
#
# queue = deque([i for i in range(1, N+1)])
#
# check = True
#
# while True:
#     if len(queue) == 1:
#         break
#
#     if check == True:
#         queue.popleft()
#         check = False
#     elif check == False:
#         queue.append(queue.popleft())
#         check = True
#
# print(queue[0])

N = int(input())
number = 2
while True:
    if N == 1 or N == 2:
        print(N)
        break
    number *= 2 # 제곱수 맞춰주기
    # 제곱수를 나눠서 빼준후 곱하면 그 값이 된다.
    if number >= N:
        print((N - (number // 2)) * 2)
        break
