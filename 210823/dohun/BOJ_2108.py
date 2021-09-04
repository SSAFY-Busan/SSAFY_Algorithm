import sys

N = int(input())
arr = []

# 입력받기
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# 정렬
arr.sort()

# 산술평균
print(round(sum(arr) / len(arr)))

# 중앙값
print(arr[N//2])

# 딕셔너리에 카운트해주기
num_cnt = {}
for i in arr:
    try:
        num_cnt[i] += 1
    except:
        num_cnt[i] = 1

# 카운트 된것 정렬
sort_cnt = sorted(num_cnt.items(),key=lambda x: x[1], reverse=True)

# 1개인 경우 1개 출력
if N == 1:
    print(sort_cnt[0][0])

# 빈도가 같으면 2번째 출력
elif sort_cnt[0][1] == sort_cnt[1][1]:
    print(sort_cnt[1][0])
# 그냥 출력
else:
    print(sort_cnt[0][0])

print(max(arr) - min(arr))