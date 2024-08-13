n = int(input())

if n == 1 or n == 3:
    print(-1)
else:
    ans = n // 5
    n %= 5
    if n % 2:
        ans -= 1
        n += 5
    print(ans + n//2)
