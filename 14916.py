#14916
#14분

n=int(input())
c5=0
c2=0



if n<2:
  print(-1)
  exit()
else:
  if n>=5:
    c5=n//5
    n=n%5
    if n%2 !=0:
      c5-=1
      n+=5
      c2=n//2
    else:
      c2=n//2
  elif n==3:
    print(-1)
    exit()
  else:
    c5=0
    c2=n//2

count= c2+c5
print(count)

