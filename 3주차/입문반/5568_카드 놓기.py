from itertools import permutations

n, k = int(input()), int(input())
cards = [input() for _ in range(n)]
num_set = set(''.join(p) for p in permutations(cards, k))

print(len(num_set))