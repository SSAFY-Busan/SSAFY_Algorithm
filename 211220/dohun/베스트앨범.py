genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []

    dic_index = {}
    dic_sum = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic_index:
            dic_index[genre] = [(idx, play)]
        else:
            dic_index[genre].append((idx, play))

        if genre not in dic_sum:
            dic_sum[genre] = play
        else:
            dic_sum[genre] += play
    print(dic_index)
    print(dic_sum)

    # 총합을 먼저 뽑아내고 높은 순으로
    for(key, value) in sorted(dic_sum.items(), key=lambda x: x[1], reverse=True):
        # print(key)
        # a = sorted(dic_index[key], key=lambda x: x[1], reverse=True)
        # print("원본",a)
        # 2개씩 모아서
        for (i, play) in sorted(dic_index[key], key=lambda x: x[1], reverse=True)[:2]:
            # print(i, play)
            answer.append(i)

    return answer

print(solution(genres,plays))