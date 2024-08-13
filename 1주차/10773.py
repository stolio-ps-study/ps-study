#10773

n=int(input())
num_list=[]

for i in range(n):
  num=int(input())
  if num == 0:
    if len(num_list)!=0:
      num_list.pop()
    continue
  else:
    num_list.append(num)

total=0
for i in range(len(num_list)):
  total+=num_list[i]
  
print(total)

