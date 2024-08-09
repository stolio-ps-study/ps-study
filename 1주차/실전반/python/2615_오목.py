def is_valid(x, y):
    return 0 <= x < 19 and 0 <= y < 19


def solve(board):
    # 각각 오른쪽, 아래쪽, 우상향 대각선, 우하향 대각선 이동
    move = ((0, 1), (1, 0), (-1, 1), (1, 1))

    for i in range(19):
        for j in range(19):
            if board[i][j] != '0':
                for dx, dy in move:
                    # 오목의 첫 번째 돌부터만 체크하도록 이전 칸이랑 같은 돌이 놓여있으면 체크 안 함
                    if is_valid(i-dx, j-dy) and board[i][j] == board[i-dx][j-dy]:
                        continue

                    # 이후 4칸이 같은 돌인지 체크
                    x, y = i+dx, j+dy
                    for _ in range(4):
                        if not is_valid(x, y) or board[i][j] != board[x][y]:
                            break
                        x, y = x+dx, y+dy
                    else:
                        # 4칸동안 같은 돌이었을 경우, 그 다음칸까지 한번 더 체크해서 육목방지
                        if not is_valid(x, y) or board[i][j] != board[x][y]:
                            print(board[i][j])
                            print(i+1, j+1)
                            return
    print(0)


solve([input().split() for _ in range(19)])

