# 후위 표기식2
N = int(input())
text = input()

# 피연산자 대응하는  값 연결하기

s = []  # 피연산자 리스트
for i in text:
    if 'A' <= i <= 'Z':
        s.append(i)
nums = {}  # 피연산자 대응하는 값
for i in s:
    if i in nums.keys():
        continue
    nums[i] = int(input())

# 연산하기
stack = []
for i in text:
    if 'A' <= i <= 'Z':
        stack.append(nums[i])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)
        elif i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
print('{:.2f}'.format(stack.pop()))
