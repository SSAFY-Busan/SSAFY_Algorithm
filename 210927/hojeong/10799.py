# 쇠막대기
s = input()
p = 0  # 자르면 생기는 조각
total = 0  # 총 조각수
for i in range(len(s) - 1):
    if s[i] == '(':
        if s[i + 1] == ')':
            total += p
        else:
            p += 1
            total += 1
    else:
        if i > 0 and s[i - 1] == ')':
            p -= 1
print(total)
