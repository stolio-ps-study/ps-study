#1316
#똑같은 알파벳이 떨어져서 나타나면 그룹단어가 아님
#똑같은 단어 거리가 절대값 1보다 크면 그룹단어가 아님 

num=int(input())
total=0


for i in range(num):
   a=input()
   b=list(a)

   for j in range(len(a)):
    first=a.find(b[j])
    last=a.rfind(b[j])
    distance= last- first

    group= True
    if distance > 1:
      for k in range(first+1,last):
        if b[k] !=  b[j]:
          group = False
          break
      if group == False:
        break

   if group==True:   
    total+=1


print(total)


