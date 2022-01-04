from collections import deque

def solution(n, edge):
    g=[[] for _ in range(n+1)]
    for a,b in edge:
        g[a].append(b)
        g[b].append(a)
    l=[0 for _ in range(n+1)]
    visited=[False]*(n+1)
    def bfs():
        visited[1]=True
        q=deque()
        q.append([g[1],0])
        while q:
            t=q.popleft()
            t[1]+=1
            for i in t[0]:
                if not visited[i]:
                    l[i]=t[1]
                    visited[i]=True
                    q.append([g[i],t[1]+1])

    bfs()
    MAX=max(l)
    return l.count(MAX)