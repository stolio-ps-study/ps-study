import sys
input = sys.stdin.readline

towns = [tuple(map(int, input().split())) for _ in range(int(input()))]
towns.sort()

people = sum(a for x, a in towns)
half = people/2

for x, a in towns:
    people -= a
    if people <= half:
        print(x)
        break