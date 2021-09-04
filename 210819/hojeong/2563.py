# 색종이
N = int(input())
# 100*100 배열에 0값으로 초기화
box = [[0] * 100 for _ in range(100)]

for i in range(N):
    C, R = map(int, input().split())  # C는 열, R은 행
    for c in range(C, C + 10):  # 색종이의 크기는 고정되어있으므로
        for r in range(R, R + 10):
            box[r][c] += 1  # 1씩 더해주기
cnt = 0

for r in range(100):
    for c in range(100):
        if box[r][c] >= 1:
            cnt += 1
print(cnt)

# total_cnt=0 # 중복된 넓이*겹침 횟수
# cnt=0 # 중복된 넓이
#
# for r in range(100):
#     for c in range(100):
#         if box[r][c]!=1 and box[r][c]!=0:
#             total_cnt+=box[r][c]
#             cnt+=1
#
# total=100*N-total_cnt+cnt #전체 넓이= 색종이넓이*색종이개수-중복된 넓이*중복 횟수 +중복된 넓이
# print(total)

# ------------------------스터디 내용--------------------
# 해당값을 1 더해주는 것이 아니라 1로 지정하여 최종 넓이를 구할때 1인것만 찾으면 된다.

# for i in range(N):
#     C, R = map(int, input().split())  # C는 열, R은 행
#     for c in range(C, C + 10):  # 색종이의 크기는 고정되어있으므로
#         for r in range(R, R + 10):
#             box[r][c] = 1  # 1로 지정
# cnt = 0
#
# for r in range(100):
#     for c in range(100):
#         if box[r][c] :
#             cnt += 1
