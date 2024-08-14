import sys
input = sys.stdin.readline

N, M = map(int, input().split())
character = {}
num = 1
quiz = []

for i in range(N + M):
    S = input().strip()
    if i < N:
        character[num] = S
        num += 1
    else:
        quiz.append(S)

reverse_character = {v: k for k, v in character.items()}

for j in quiz:
    if j.isdigit():
        print(character[int(j)])
    else:
        print(reverse_character[j])