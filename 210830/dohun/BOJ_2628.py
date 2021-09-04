width, height = map(int, input().split())
T = int(input())

width_lst = [0, width]
height_lst = [0, height]

for _ in range(T):
    number, idx = map(int, input().split())
    if number == 1:
        width_lst.append(idx)
    else:
        height_lst.append(idx)

width_lst.sort()
height_lst.sort()

answer = []
for i in range(1, len(width_lst)):
    for j in range(1, len(height_lst)):
        a = width_lst[i] - width_lst[i-1]
        b = height_lst[j] - height_lst[j-1]
        answer.append(a*b)

max_value = max(answer)

print(max_value)