genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
check = {}
# {'classic': [1450, {0: 500, 2: 150, 3: 800}], 'pop': [3100, {1: 600, 4: 2500}]}
for i in range(len(genres)):
    if check.get(genres[i]):
        check[genres[i]][0] += plays[i]
        check[genres[i]][1][i] = plays[i]
    else:
        check[genres[i]] = [plays[i], {i: plays[i]}]
print(check)
check = sorted(check.items(), key=lambda x: x[1], reverse=True)
# [('pop', [3100, {1: 600, 4: 2500}]), ('classic', [1450, {0: 500, 2: 150, 3: 800}])]

print(check)
ans = []
for i in range(len(check)):
    # print(check[i][1][1])
    answer = sorted(check[i][1][1].items(), key=lambda x: x[1], reverse=True)
    # print(answer)
    if len(answer) >= 2:
        ans.append(answer[0][0])
        ans.append(answer[1][0])
    else:
        ans.append(answer[0][0])
print(ans)
