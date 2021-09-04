N = int(input())
words = []

# 리스트에 입력받기
for _ in range(N):
    words.append(input())
    # 튜플형태로 입력을 받기
    # words.append((word, len(word)))

# 중복 제거
words = list(set(words))
# 정렬을 하는데  길이 -> 단어순으로 정렬
sort_words = sorted(words, key=lambda x: (len(x), x))

# 출력
for i in sort_words:
    print(i)