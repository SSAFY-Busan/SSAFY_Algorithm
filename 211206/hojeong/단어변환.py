from collections import deque


def solution(begin, target, words):
    l = len(words)

    def bfs():
        q = [[begin, 0]]  # 시작문자, 변환횟수
        q = deque(q)
        visited = [0 for _ in range(l)]  # 방문체크
        while q:
            t = q.popleft()
            if t[0] == target:  # 타겟문자랑 같아지면
                return t[1]  # 그때의 변환횟수 반환
            for i in range(l):
                t_count = 0  # 다른 알파벳 수 찾기
                for j in range(len(t[0])):
                    if t[0][j] != words[i][j]:
                        t_count += 1
                if t_count == 1 and not visited[i]:  # 한글자만 다르고 방문안했으면
                    visited[i] = 1  # 방문체크
                    q.append([words[i], t[1] + 1])  # 추가

    answer = bfs()
    if answer:
        return answer
    else:
        return 0
