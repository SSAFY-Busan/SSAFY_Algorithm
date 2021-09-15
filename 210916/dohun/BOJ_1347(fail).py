# 틀린코드

# 남 서 북 동
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())

# 이동
lst = list(input())

direction = 0
x, y = 0, 0
graph = [[x,y]]

for move in lst:
    if move == 'F':
        x += dx[direction]
        y += dy[direction]
        graph.append([x,y])
    elif move == 'R':
        direction += 1
        if direction == 4:
            direction = 0
    else:
        direction -= 1
        if direction == -1:
            direction = 3

row_lst = []
col_lst = []
for i in graph:
    col_lst.append(i[1]) # 가로 모으기
    row_lst.append(i[0]) # 세로 모으기

row = len(set(row_lst))
col = len(set(col_lst))
row_check = False
col_check = False
for i in range(row):
    if row_lst[i] < 0:
        row_lst[i] = row_lst[i] * -1
        row_check = True

for i in range(col):
    if col_lst[i] < 0:
        col_lst[i] = col_lst[i] * -1
        col_check = True

graph = [['#'] * col for _ in range(row)]

for i in range(len(row_lst)):
    graph[row_lst[i]][col_lst[i]] = '.'

answer = []

for i in range(len(graph)-1, -1, -1):
    answer.append(graph[i])

for i in answer:
    print(''.join(i))