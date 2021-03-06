# 바이러스

# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와
# 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지
# 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와
# 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다. 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게
# 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩
# 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.


def dfs(i):                                  # dfs
    visited[i] = 1                           # 방문체크 1
    for j in tree[i]:                        # 트리의 각 요소를 탐색해서
        if visited[j] == 0:                  # 방문한게 없다면
            ans.append('1')                  # 1을 추가하고 다시 탐색
            dfs(j)                           # j 를 다시해서 탐색을 계속한다.


N = int(input())                             # 컴퓨터의 수          
n = int(input())                             # 노드의 수 
tree = [[] for _ in range(N+1)]              # 트리
visited = [0 for _ in range(N+1)]            # 방문할 배열
ans = []                                     # 정답 리스트
for i in range(n):                           # 노드만큼 반복
    a, b = list(map(int, input().split()))   # 노드 추가
    tree[a].append(b)                        # 트리에 양방향으로 추가
    tree[b].append(a)
dfs(1)                                       # 1이 바이러스 걸렷으니깐 1부터
print(len(ans))                              # 정답리스트의 개수