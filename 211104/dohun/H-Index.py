citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort()
    # 전체 논문 횟수
    book = len(citations)

    # citations[i] 는 논문이 인용된 횟수
    # book - i는 인용된 논문의 최대 개수에서 줄여나가는 숫자
    for i in range(book):
        if citations[i] >= book - i:
            return book - i
    # 없으면 0 반환
    return 0

print(solution(citations))