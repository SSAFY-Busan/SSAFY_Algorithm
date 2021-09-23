# 문자열 집합

# 총 N개의 문자열로 이루어진 집합 S가 주어진다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

# 첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.
# 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
# 다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
# 입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다.
# 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.
import sys

N, M = list(map(int, sys.stdin.readline().split())) #  개수 입력
S = []                    # 검사 리스트
for i in range(N):        # 검사 리스트에 추가
    s = input()
    S.append(s)
checks = 0                # 검사해서 있는 수
for i in range(M):        # 반복해서
    check = input()       # 입력받은게
    if  check in S:       # S 에 있으면
        checks += 1       # 1씩 추가
print(checks)             # 출력