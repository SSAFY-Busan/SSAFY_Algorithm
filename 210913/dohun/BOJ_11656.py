word = input()
lst = []

for i in range(len(word)):
    lst.append(word[i:])

lst.sort()

for word in lst:
    print(word)