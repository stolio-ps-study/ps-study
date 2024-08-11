n, m, b = map(int, input().split())
counts = [0] * 257

for _ in range(n):
    for h in map(int, input().split()):
        counts[h] += 1

min_height = 0
max_height = 256

for i, num in enumerate(counts):
    if num:
        min_height = i
        break

for i, num in enumerate(counts[::-1]):
    if num:
        max_height = 256-i
        break

t = 0
while min_height != max_height:
    if (min_count:=counts[min_height]) <= (max_count:=counts[max_height]) * 2 and b >= min_count:
        b -= min_count
        t += min_count
        counts[min_height+1] += min_count
        counts[min_height] = 0
        min_height += 1
    else:
        b += max_count
        t += max_count * 2
        counts[max_height-1] += max_count
        counts[max_height] = 0
        max_height -= 1

print(t, min_height)