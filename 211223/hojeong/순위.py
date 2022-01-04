n=5
results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
win = [set() for _ in range(n + 1)]
lose = [set() for _ in range(n + 1)]

for winner, loser in results:
    win[winner].add(loser)
    lose[loser].add(winner)

for i in range(1, n + 1):
    for winner in lose[i]:
        win[winner].update(win[i])
    for loser in win[i]:
        lose[loser].update(lose[i])

# 시간 초과
# for i in range(1,n+1):
#     win[i]=set(win[i])
#     lose[i]=set(lose[i])

# 길이가 n-1이면 순위 확정
cnt = 0
for i in range(1, n + 1):
    if len(win[i]) + len(lose[i]) == n - 1:
        cnt += 1
print(cnt)