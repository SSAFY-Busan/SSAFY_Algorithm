N = int(input())
cnt = 0

for _ in range(N):
    words = input()
    stack = []

    for word in range(len(words)):
        if stack:
            if words[word] == stack[-1]:
                stack.pop()
            else:
                stack.append(words[word])
        else:
            stack.append(words[word])

    if len(stack) == 0:
        cnt += 1
print(cnt)