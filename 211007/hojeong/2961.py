# 도영이가 만든 맛있는 음식

def cook(temp1, temp2):
    global ans
    for i in sel:
        temp1 *= foods[i][0]
        temp2 += foods[i][1]

    if ans > abs(temp1 - temp2):
        ans = abs(temp1 - temp2)


def comb(idx, s_idx):
    if s_idx == R:
        cook(1, 0)
        print(sel)
        return
    elif idx == N:
        return
    else:
        sel[s_idx] = idx
        comb(idx + 1, s_idx + 1)
        comb(idx + 1, s_idx)


N = int(input())
foods = [list(map(int, input().split())) for _ in range(N)]

ans = 999999999
# 1개 이상 뽑기
for i in range(1, N + 1):
    R = i
    sel = [0] * R
    comb(0, 0)

print(ans)
