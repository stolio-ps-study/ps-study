#1620
#53분


N,M=map(int,input().split())
dic_num={}
dic_name={}
answer=[]

for i in range(1,N+M+1):
  Q=input()
  if i<=N:
    dic_name[Q]=str(i)
    dic_num[i]=Q
  else: 
    if Q.isdigit():
      answer.append(dic_num[int(Q)])
    else:
      answer.append(dic_name[Q])
    
  
print("\n".join(answer))
  
