ans = 0

for _ in range(int(input())):
    before = ''
    appeared = set()
    for c in input():
        if c != before:
            if c in appeared:
                break
            before = c
            appeared.add(c)
    else:
        ans += 1

print(ans)
