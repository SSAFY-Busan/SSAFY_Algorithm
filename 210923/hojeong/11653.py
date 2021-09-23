# 소인수분해
N = int(input())
if N == 1:  # N이 1이면
    print()  # 아무것도 출력 안함
else:
    lst = []  # 소인수를 담을 리스트
    while N != 1:  # 나눌 값이 1이 되면 종료
        for i in range(2, N + 1):  # 2부터 N까지 순회
            if N % i == 0:  # 나눠 떨어진다며
                lst.append(i)  # 리스트에 추가
                N //= i  # N은 나눈 몫으로 갱신
                break  # 반복문 탈출해서 다시 2부터 탐색
    for i in lst:
        print(i)
