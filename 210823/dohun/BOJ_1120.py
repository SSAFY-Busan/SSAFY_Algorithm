A, B = input().split()
min_value = len(A)
# 인덱스가 초과하지 않게 맞춰준다.
for i in range(len(B)-len(A)+1):
    cnt = 0
    # 작은것인 A의 길이만큼 반복하면서 길이 비교해준다.
    for j in range(len(A)):
        # 다른 문자가 올 경우 횟수 1번 추가
        if A[j] != B[i+j]:
            cnt += 1
    # 최소보다 작으면 계속 갱신한다.
    if cnt < min_value:
        min_value = cnt
print(min_value)