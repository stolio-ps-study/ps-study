#1620_나는야 포켓몬 마스터 이다솜
import sys

n, m = map(int, input().split())
poke_num={}
poke_name={}

for i in range(1, n+1):
    a=sys.stdin.readline().strip()
    poke_num[i]=a
    poke_name[a]=i

for _ in range(m):
    p=sys.stdin.readline().strip()
    if p.isdigit()==True:
        print(poke_num[int(p)])
    else:
        print(poke_name[p])
