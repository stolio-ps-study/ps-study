from sys import stdin
from collections import Counter

input = stdin.readline

n, m = map(int, input().split())
words = Counter(filter(lambda x: len(x) >= m, (input().rstrip() for _ in range(n))))

print(*sorted(words.keys(), key=lambda x: (-words[x], -len(x), x)), sep='\n')
