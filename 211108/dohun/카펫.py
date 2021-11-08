def solution(brown, yellow):
    # 전체 사각형 넓이
    square = brown + yellow

    # 사각형 길이 찾기
    for i in range(square, 1, -1):
        # 나누어 진다면 높이가 나옴
        if square % i == 0:
            h = square // i
            # 높이-2, 가로-2 곱한게 yellow 라면 yellow 사각형이다.
            if (h - 2) * (i - 2) == yellow:
                return [i, h]

brown, yellow = 10, 2
print(solution(brown, yellow))