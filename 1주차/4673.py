def d(n):
    length = len(str(n))
    tmp = 0
    for i in range(length):
        tmp += int(str(n)[i])
    return n + tmp

self_numbers = []

for num in range(1, 10001):
    result = d(num)
    if result <= 10000:
        self_numbers.append(result)

for i in range(1, 10001):
    if i not in self_numbers:
        print(i)
