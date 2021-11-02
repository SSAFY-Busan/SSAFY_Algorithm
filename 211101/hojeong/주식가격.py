from collections import deque

def solution(prices):
    answer = []
    q=deque(prices)
    while q:
        t = q.popleft()
        cnt = 0
        for i in q:
            if i >= t:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer
