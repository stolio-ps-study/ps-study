#2941
#크로아티아 영어 치환
c=['c=','c-','dz=','d-','lj','nj','s=','z=']
str=input()

for i in range(len(c)):
  if str.find(c[i])!=-1:
    str=str.replace(c[i],'a')

print(str)
print(len(str))

