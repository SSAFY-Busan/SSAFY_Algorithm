def score(arr, l, answers):
    s = 0
    for i in range(l):
        if arr[i] == answers[i]:
            s += 1
    return s


def solution(answers):
    answer = []
    l = len(answers)

    # 패턴
    a = [1, 2, 3, 4, 5]
    b = [1, 3, 4, 5]
    c = [3, 1, 2, 4, 5]

    # 찍는 방식
    p1 = [0] * l
    p2 = [0] * l
    p3 = [0] * l
    for i in range(l):
        p1[i] = a[i % 5]
        if i % 2:
            p2[i] = b[(i // 2) % 4]
        else:
            p2[i] = 2
        p3[i] = c[(i // 2) % 5]

    # 점수
    s1 = score(p1, l, answers)
    s2 = score(p2, l, answers)
    s3 = score(p3, l, answers)

    # 1등
    MAX = max(s1, s2, s3)
    if s1 == MAX:
        answer.append(1)
    if s2 == MAX:
        answer.append(2)
    if s3 == MAX:
        answer.append(3)

    return answer