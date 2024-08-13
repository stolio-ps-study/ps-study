n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
for i in a[::-1]:
    if i <= k:
        ans += k//i
        k %= i
print(ans)