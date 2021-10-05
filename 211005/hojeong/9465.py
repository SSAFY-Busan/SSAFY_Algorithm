# 스티커
T = int(input())
for tc in range(T):
    n = int(input())  # 열
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]

    for c in range(1, n):
        for r in range(2):
            if 0 <= c - 2:
                dp[r][c] = max(dp[r - 1][c - 1], dp[r - 1][c - 2]) + stickers[r][c]
            else:
                dp[r][c] = dp[r - 1][c - 1] + stickers[r][c]
    print(max(dp[0][-1], dp[1][-1]))
