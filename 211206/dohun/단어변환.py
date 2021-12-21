begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    answer = 0
    queue = []
    queue.append((begin, 0))
    # 타겟이 단어목록에 없으면 0 반환
    if target not in words:
        return 0

    while queue:
        now, idx = queue.pop(0)
        for word in words:
            diff = 0
            # 단어를 탐색하면서 차이 찾기
            for i in range(len(word)):
                if now[i] != word[i]:
                    diff += 1
            # 차이가 1인데 타겟에 도달하면 탈출
            if diff == 1 and word == target:
                idx += 1
                return idx
            # 1개만 다르면 다시 넣어주기
            elif diff == 1:
                queue.append((word, idx+1))

    return answer


print(solution(begin, target, words))