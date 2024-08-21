import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph:
    edges.sort(reverse=True)

visited = [False] * (n+1)
stk = [v]
ans = []
while stk:
    now = stk.pop()
    if not visited[now]:
        visited[now] = True
        ans.append(now)
        stk += graph[now]
print(*ans)

visited = [False] * (n+1)
visited[v] = True
stk = [v]
ans = []
while stk:
    tmp = []
    for now in stk:
        ans.append(now)
        for after in reversed(graph[now]):
            if not visited[after]:
                visited[after] = True
                tmp.append(after)
    stk = tmp
print(*ans)