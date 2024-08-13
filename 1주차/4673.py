#4673

num_list=[]
for i in range(1,10001):
  num_str=str(i)
  for j in range(len(num_str)):
    i+= int(num_str[j])
  num_list.append(i)

a=set(num_list) #set: 리스트 중복 제거
b=[]
for i in range(1,10001):
  b.append(i)

result=list(set(b)-a)
result.sort() #sort는 none을 반환 


for i in range(len(result)):
  print(result[i])
  