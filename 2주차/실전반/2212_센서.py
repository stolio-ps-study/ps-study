n, k = int(input()), int(input())
sensors = sorted((map(int, input().split())))

dist = sorted(sensors[i]-sensors[i-1] for i in range(1, len(sensors)))

print(sum(dist[:n-k]))
