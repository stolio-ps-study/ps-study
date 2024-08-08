self_num = [False] + [True] * 10000

for n in range(1, 10000):
    dn = n + sum(map(int, str(n)))
    if dn <= 10000:
        self_num[dn] = False

print(*(i for i, is_self_num in enumerate(self_num) if is_self_num), sep='\n')
