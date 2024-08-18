from collections import deque


def to_string(graph):
    return ''.join(''.join(i) for i in graph)


graph = [list(input().split()) for _ in range(3)]
s = to_string(graph)
dic = {s: 0}
ans = '123456780'

move = ((0, 1), (1, 0), (0, -1), (-1, 0))

queue = deque(((s, 0),))
while queue:
    s, cnt = queue.popleft()
    graph = [list(s[i*3:i*3+3]) for i in range(3)]
    zero = s.find('0')
    x, y = zero // 3, zero % 3
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            new_s = to_string(graph)
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            if new_s not in dic:
                dic[new_s] = cnt+1
                queue.append((new_s, cnt+1))
                if new_s == ans:
                    queue = []
                    break

print(dic[ans] if ans in dic else -1)
