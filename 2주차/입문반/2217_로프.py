from sys import stdin
input = stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()
print(max(rope*(n-i) for i, rope in enumerate(ropes)))