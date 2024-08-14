def money(n):
    for i in range(n // 5, -1, -1):
        first = n - (i * 5)
        if first % 2 == 0:
            return i + (first // 2)
    return -1

n = int(input())
print(money(n))
