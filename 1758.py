#1758
#최댓값-> 큰수를 앞에 작은 수를 뒤에
#팁 = 돈 - (받은 등수-1)
#17분

N=int(input())
num=[0]*N

for i in range(N):
  num[i]=int(input())

num.sort(reverse=True)
sum=0

for i in range(N):
  result=num[i]-i
  if result<0:
    result=0

  sum+=result

print(sum)
