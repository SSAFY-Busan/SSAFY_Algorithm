def solution(N, number):
    check = [0, [N]]
    for i in range(2, 9):
        temp = set()
        temp.add(int(str(N) * i))
        for j in range(1, i):
            for x in check[j]:
                for y in check[i - j]:
                    temp.add(x + y)
                    temp.add(x - y)
                    temp.add(x * y)
                    temp.add(y - x)
                    if y != 0:
                        temp.add(x // y)
                    if x != 0:
                        temp.add(y // x)
        check.append(temp)
    for i in range(1, len(check)):
        if number in check[i]:
            answer = i
            break
    else:
        answer = -1
    return answer
