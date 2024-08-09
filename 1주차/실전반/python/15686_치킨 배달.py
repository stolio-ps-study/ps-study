from itertools import combinations

n, m = map(int, input().split())

house, chicken = [], []

for i in range(n):
    for j, num in enumerate(input().split()):
        if num == '1':
            house.append((i, j))
        elif num == '2':
            chicken.append((i, j))

ans = float('inf')
for selected_chicken in combinations(chicken, m):
    distance = sum(min(abs(h[0]-c[0])+abs(h[1]-c[1]) for c in selected_chicken) for h in house)
    ans = min(ans, distance)

print(ans)