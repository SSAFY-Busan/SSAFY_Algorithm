# 무한이진트리

# 다음과 같은 귀납적인 규칙에 의해서 만들어지는 무한한 크기의 이진 트리를 생각하자.
# 각각의 노드에는 두 정수의 순서쌍이 할당되어 있다.
# 루트에는 (1, 1)이 할당된다.
# 어떤 노드가 (a, b)가 할당되었을 때, 그 노드의 왼쪽 자식에는 (a+b, b)가 할당되고, 오른쪽 자식에는 (a, a+b)가 할당된다.
# 우리는 어떤 노드가 주어졌을 때, 루트에서 그 노드로 이동하는 최단 경로를 찾으려 한다.
# 하지만 최단 경로가 매우 길 수도 있기 때문에, 왼쪽 자식으로 이동하는 회수와 오른쪽 자식으로 이동하는 회수를 찾으려고 한다.
# 입력으로 두 정수 A, B가 주어졌을 때, 루트에서 (A, B)가 할당된 노드까지 최단 경로로 이동할 때,
# 왼쪽 자식으로 이동하는 회수와 오른쪽 자식으로 이동하는 회수를 구해내는 프로그램을 작성하시오.

# 첫째 줄에 두 정수 A, B(1≤A, B≤2,000,000,000)가 주어진다. 잘못된 입력은 주어지지 않는다고 가정한다.
import sys

A, B = sys.stdin.readline().split()     # A B 두수 입력
a = int(A)                              # 인트로 변형
b = int(B)      
cnt_L = 0                               # 왼쪽 트리의 수 
cnt_R = 0                               # 오른쪽 트리의 수
while True:                             # 반복
    if a == 1 and b == 1:               # 두 숫자가 1이면 멈춰
        break
    if a == 1:                          # a 가 1이면 오른쪽 트리의 수는 b - 1
        cnt_R += (b-1)
        break                           # 멈춰
    if b == 1:                          # b 가 1이면 왼쪽 트리의 수는 b - 1
        cnt_L += (a-1)
        break                           # 멈춰
    if a > b:                           # a 가 크면
        a = a - b                       # a 가 a+b 로 인해 a 로된것이니깐 a-b로 전단계로 변경
        cnt_L += 1                      # 왼쪽트리의 수를 1 증가
    if a < b:                           # b 가 크면
        b = b - a                       # b 가 a+b 로 인해 b 로된것이니깐 b-a 로 전단계로 변경
        cnt_R += 1                      # 오른쪽트리의 수를 1 증가

print(cnt_L, cnt_R)