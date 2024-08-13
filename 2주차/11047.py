# 11047 동전 0

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
cnt=0

coin.sort(reverse=True)

for c in coin:
    cnt+=(k//c)
    k%=c

print(cnt)