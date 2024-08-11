n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [input().split() for _ in range(n)]

move = ((-1, 0), (0, 1), (1, 0), (0, -1))

ans = 0
while True:
    if room[r][c] == '0':
        room[r][c] = '-1'
        ans += 1

    for _ in range(4):
        d = (d - 1) % 4
        dr, dc = move[d]
        nr, nc = r + dr, c + dc
        if 0 < nr <= n and 0 < nc <= m and room[nr][nc] == '0':
            r, c = nr, nc
            break
    else:
        dr, dc = move[d]
        nr, nc = r - dr, c - dc
        if 0 < nr <= n and 0 < nc <= m and room[nr][nc] != '1':
            r, c = nr, nc
        else:
            break


print(ans)