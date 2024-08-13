#1920

N=int(input())
n=set(map(str,input().split())) 

M=int(input())
m=list(map(str,input().split()))


for i in m:
  if i in n:
    answer=1
  else:
    answer=0
  print(answer)





