number = list(map(int, input().split()))
N = number[0]
K = number[1]

arrays = [int(input()) for i in range(N)]
arrays.sort(reverse=True)

coin_count = 0

for coin in arrays:
    if K == 0:
        break
    coin_count += K // coin
    K %= coin

print(coin_count)
