N = int(input())
table = []

for _ in range(N):
    x, y = map(int, input().split())
    table.append((x, y))

rank = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if i != j:
            if table[i][0] < table[j][0] and table[i][1] < table[j][1]:
                cnt += 1
    rank.append(cnt)

print(rank.join(" "))

