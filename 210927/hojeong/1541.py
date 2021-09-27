# 잃어버린 괄호
s = input().split('-')  # '-' 를 기준으로 나눠서 입력 받기 ['55', '50+40']
for i in range(len(s)):
    # + 먼저 처리 해주기
    if '+' in s[i]:
        s[i] = s[i].split('+')
        temp = 0  # 두수의 합
        for j in range(len(s[i])):
            temp += int(s[i][j])
        s[i] = temp  # 구한 값으로 갱신
ans = int(s[0])  # 처음 값으로 초기화
for i in range(1, len(s)):
    ans -= int(s[i])  # 더한 값들을 빼줌
print(ans)
