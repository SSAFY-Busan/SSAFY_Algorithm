def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    p = list(range(n))
    ans = 0
    pick = 0
    idx = 0

    def find_set(x):
        if p[x] != x:
            p[x] = find_set(p[x])
        return p[x]

    def union(x, y):
        p[find_set(y)] = find_set(x)

    while pick < n - 1:
        x = costs[idx][0]
        y = costs[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            pick += 1
            ans += costs[idx][2]

        idx += 1
    return ans