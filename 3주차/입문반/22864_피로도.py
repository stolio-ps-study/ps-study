a, b, c, m = map(int, input().split())
fatigue = 0

ans = 0
for _ in range(24):
    if fatigue+a <= m:
        ans += b
        fatigue += a
    else:
        fatigue -= min(fatigue, c)
print(ans)
