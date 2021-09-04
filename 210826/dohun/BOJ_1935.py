N = int(input())
words = input()

lst = [0] * N
stack = []

for i in range(N):
    lst[i] = int(input())

for word in words:
    if 'A' <= word <= 'Z':
        stack.append(lst[ord(word) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()

        if word =='+':
            stack.append(a+b)
        elif word =='-':
            stack.append(a-b)
        elif word =='*':
            stack.append(a*b)
        elif word == '/':
            stack.append(a / b)

print("{:.2f}".format(stack[0]))