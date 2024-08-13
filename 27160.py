#27160
#22분

N=int(input())

sn, bn, ln, pn =0,0,0,0

for i in range(N):
  S,sX = map(str,input().split())
  X= int(sX)
  if S == 'STRAWBERRY':
    sn+=X
  elif S=='BANANA':
    bn+=X
  elif S=='LIME':
    ln+=X
  elif S=='PLUM':
    pn+=X


if sn ==5 or bn==5 or ln==5 or pn == 5:
  print('YES')
else:
  print('NO')
