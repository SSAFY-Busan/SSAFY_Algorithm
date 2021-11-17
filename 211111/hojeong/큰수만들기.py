def solution(number, k):
    stack = []

    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)

    # k가 남아있는 경우( 생략시 12번 테스트 실패,,)
    if k > 0:
        stack = stack[:len(stack) - k]
    return ''.join(stack)