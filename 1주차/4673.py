def d(n):
    num = n
    while n > 0:
        num += n % 10
        n //= 10
    return num

generated_numbers = []

for i in range(1, 10001):
    generated_numbers.append(d(i))

for i in range(1, 10001):
    if i not in generated_numbers:
        print(i)