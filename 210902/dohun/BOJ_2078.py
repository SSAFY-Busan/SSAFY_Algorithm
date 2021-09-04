import sys
input = sys.stdin.readline

a, b = map(int, input().split())
x, y = 0, 0

while True:
    if a == 1 and b == 1:
        break

    if a == 1:
        y += (b-1)
        break

    if b == 1:
        x += (a-1)
        break

    if a > b:
        x += 1
        a = a - b

    if a < b:
        y += 1
        b = b - a

print(x,y)
