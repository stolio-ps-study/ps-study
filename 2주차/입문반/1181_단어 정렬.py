from sys import stdin
input = stdin.readline

words = [input().rstrip() for _ in range(int(input()))]
print('\n'.join(sorted(set(words), key=lambda x:(len(x), x))))