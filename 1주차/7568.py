#7568
#덩치가 크다 -> 몸무게, 키 다 커야함

n=int(input())
D={}

for i in range(n):
  weight, height = map(int,input().split())
  D[i]=[weight, height]

lst=[]

for i in range(n):
  count=1
  for j in range(n):
    if list(D[i])[0] < list(D[j])[0] and list(D[i])[1] < list(D[j])[1]:
      count+=1
    else:
      continue
  lst.append(count)

result=' '.join(map(str,lst))
print(result)



