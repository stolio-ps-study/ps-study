# 20920 영단어 암기는 괴로워
import sys

n, m = map(int, sys.stdin.readline().split())
d={}

for _ in range(n):
    w = input().strip()
    if len(w) < m:
        continue
    else:
        if w in d:
            d[w]+=1
        else:
            d[w]=1

# 모르겠어서 블로그좀 참고함
# 다중 조건 정렬

d=sorted(d.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in d:
    print(i[0])
