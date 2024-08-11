# 보드의 x행과 y열에서 가장 긴 같은 색 사탕의 길이를 찾는 함수
def find_longest(board, x, y):
    ans = 1
    tmp_r, tmp_c = 1, 1
    for i in range(1, len(board)):
        if board[x][i] != board[x][i-1]:
            ans = max(ans, tmp_r)
            tmp_r = 1
        else:
            tmp_r += 1
        if board[i][y] != board[i-1][y]:
            ans = max(ans, tmp_c)
            tmp_c = 1
        else:
            tmp_c += 1
    return max(ans, tmp_r, tmp_c)


n = int(input())
board = [list(input()) for _ in range(n)]

d = ((1, 0), (0, 1))
ans = 0

for i in range(n):
    ans = max(ans, find_longest(board, i, i))
    for j in range(n):
        for dx, dy in d:
            if 0 <= (nx:=i+dx) < n and 0 <= (ny:=j+dy) < n and board[i][j] != board[nx][ny]:
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                ans = max(ans, find_longest(board, nx, ny), find_longest(board, i, j))
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
        if ans == n:
            break
    if ans == n:
        break

print(ans)