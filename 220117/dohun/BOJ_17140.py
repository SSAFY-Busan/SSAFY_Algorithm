R, C, K = map(int, input().split())

graph = []

for _ in range(3):
    graph.append(list(map(int, input().split())))

time = 0
check = False
while time <= 100:
    if R <= len(graph) and C <= len(graph[0]) and graph[R-1][C-1] == K:
        print(time)
        check = True
        break

    time += 1
    max_column = 0
    next_lst = []

    # R연산하기
    if len(graph) >= len(graph[0]):
        for rows in graph:
            row_lst = []
            row_dic = {}
            # 빈도 체크해주기
            for row in rows:
                if row in row_dic:
                    row_dic[row] += 1
                else:
                    row_dic[row] = 1
            sort_row = sorted(row_dic.items(), key=lambda x: (x[1], x[0]))
            for number, cnt in sort_row:
                if number == 0:
                    continue
                row_lst.append(number)
                row_lst.append(cnt)
            # 최대길이 찾기
            max_column = max(max_column, len(row_lst))
            next_lst.append(row_lst)
        # print("여기도", next_lst)
        # print("맥스", max_column)

        # 0채워넣기
        for rows in next_lst:
            if len(rows) < max_column:
                for _ in range(max_column - len(rows)):
                    rows.append(0)
        graph = next_lst
        # print("보자", graph)
        continue
    # C연산
    elif len(graph) < len(graph[0]):
        # print("세로 시작")
        graph = list(map(list, zip(*graph)))

        # print("돌려보자", graph)
        for rows in graph:
            row_lst = []
            row_dic = {}
            # 체크해주기
            for row in rows:
                if row in row_dic:
                    row_dic[row] += 1
                else:
                    row_dic[row] = 1

            sort_row = sorted(row_dic.items(), key=lambda x: (x[1], x[0]))
            # print("여긴?", sort_row)
            for number, cnt in sort_row:
                if number == 0:
                    continue
                row_lst.append(number)
                row_lst.append(cnt)
            max_column = max(max_column, len(row_lst))
            next_lst.append(row_lst)
        # print("다음을 보자", next_lst)

        # 0채워넣기
        for rows in next_lst:
            if len(rows) < max_column:
                for _ in range(max_column - len(rows)):
                    rows.append(0)
        # print("얼마나", next_lst)

        # grpah = list(map(list, zip(*next_lst)))
        lst = []
        for i in zip(*next_lst):
            lst.append(list(i))
        # print("리스트", lst)
        # print("돌려라", graph)
        graph = lst
        continue

if check == False:
    print(-1)