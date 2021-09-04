N = int(input())

max_value = 0
lst = []

for i in range(N+1):
    answer = [N, i]
    # 인덱스 카운트
    idx = 0
    while True:
        x = answer[idx] - answer[idx+1]
        # 음수면 끝
        if x < 0:
            break
        # 아닐경우 값 계속 추가
        answer.append(x)
        
        # 최대길이 갱신
        if len(answer) > max_value:
            max_value = len(answer)
            lst.append(answer)
        idx += 1

print(max_value)
for i in lst[-1]:
    print(i, end=' ')

