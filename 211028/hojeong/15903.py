# 카드 합체 놀이
n, m = map(int, input().split())
cards = list(map(int, input().split()))
cnt = 0
while cnt < m:
    cnt += 1
    cards.sort()
    a = cards.pop(0)
    b = cards.pop(0)
    cards.append(a + b)
    cards.append(a + b)
print(sum(cards))
