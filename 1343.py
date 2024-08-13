# X가 홀수-> -1
# .이 있을 떄 -> .을 기준으로 나눔 -> 홀수면 -1 짝수면 바꿈
# 짝수일 떄-> X 개수를 4로 나눠서 몫이 1보다 크면 A -> 나머지: B

A=input()

Xcount=A.count('X')

if Xcount % 2 == 0:
  if '.' in A:
    A_list=A.split('.')
    for i in range(len(A_list)):
      a=A_list[i]
      if a.count('X')%2 !=0:
        print(-1)
        break
      else:
        a4=len(a)//4
        if a4 >= 1:
          a='AAAA'*a4+'B'*((len(a)%4)//2)
        elif a == '':
          continue
        else:
          a= a.replace(a,'BB')

        A_list[i]=a

    result = '.'.join(A_list)
    print(result)


  else:
    A4=len(A)//4
    if A4 >= 1:
      A='AAAA'*A4+'B'*((len(A)%4)//2)
    else:
      A= 'BB'
    print(A)

else:
  print(-1)




