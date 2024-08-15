## 딸기,바나나,라임,자두
N = int(input())
S = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}

for _ in range(N):
    card = input().split()
    if card[0] in S:
        S[card[0]] += int(card[1])

for i in S.values():
    if i == 5:
        print("YES")
        break
else:
    print("NO")
