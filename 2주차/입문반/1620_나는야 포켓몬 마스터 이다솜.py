from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
pokemon_dict = {input().rstrip(): i+1 for i in range(n)}
pokemon_keys = list(pokemon_dict.keys())
for _ in range(m):
    query = input().rstrip()
    if query.isdigit():
        print(pokemon_keys[int(query)-1])
    else:
        print(pokemon_dict[query])