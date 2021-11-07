def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            answer = i
            break
    else:
        answer = len(citations)
    return answer
