from sys import stdin
input = stdin.readline

card = {name: 0 for name in ('STRAWBERRY', 'BANANA', 'LIME', 'PLUM')}

for _ in range(int(input())):
    s, x = input().split()
    card[s] += int(x)

for cnt in card.values():
    if cnt == 5:
        print("YES")
        break
else:
    print("NO")