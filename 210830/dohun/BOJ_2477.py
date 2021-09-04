N = int(input())

width, height = 0, 0
width2, height2 = 0, 0
cnt = [0, 0, 0, 0, 0]

for i in range(6):
    direction, length = map(int, input().split())
    if i % 2 == 0:
        width = max(width, length)
    else:
        height = max(height, length)

    if i == 3:
        width2 = length
    if i == 4:
        height2 = length

print(N*(width*height - width2*height2))

#     cnt[direction] += 1
#
#     if direction == 1 or direction == 2:
#         width = max(width, length)
#     elif direction == 3 or direction == 4:
#         height = max(height, length)
#
#     for j in range(1,len(cnt)):
#         if cnt[j] == 2:
#             if j == 1 or j == 2:
#                 width2 = length
#             elif j == 3 or j == 4:
#                 height2 = length
#
# print(cnt)
# print(height, width)
# print(height2, width2)
# print(N*(width*height - width2*height2))

