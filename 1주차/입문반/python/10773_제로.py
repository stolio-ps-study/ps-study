from sys import stdin

input = stdin.readline

stack = []

for _ in range(int(input())):
    n = int(input())
    if n:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))
