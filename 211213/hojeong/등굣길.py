m=4
n=3
puddles=[[2,2]]
miro=[[0]*m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if [c + 1, r + 1] in puddles:
            miro[r][c] = 0
        elif r == 0 or c == 0:
            miro[r][c] = 1
        elif c >= 1 and r >= 1:
            miro[r][c] = (miro[r - 1][c] + miro[r][c - 1]) % 1000000007
print(miro[n-1][m-1])