number = int(input())

S = {'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}

for _ in range(number):
    card = input().upper().split()
    if card[0] in S:
        S[card[0]] += int(card[1])

found = False
for key in S:
    if S[key] == 5:
        found = True
        break

if found:
    print('YES')
else:
    print('NO')
