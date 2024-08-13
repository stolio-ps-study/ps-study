#1343
# X가 홀수-> -1
# .이 있을 떄 -> .을 기준으로 나눔 -> 홀수면 -1 짝수면 바꿈 -> 합침
# 짝수일 떄-> X 개수를 4로 나눠서 몫이 1보다 크면 A -> 나머지 2개 B
#40분


A=input()
Xcount= A.count('X')

if Xcount%2 != 0:
  print(-1)
else:
  if '.' in A:
    A=A.split('.')
    for i in range(len(A)):
      if A[i].count('X') % 2 !=0:
        print(-1)
        exit()
      elif A[i] == '':
        continue
      else:
        A[i] = 'AAAA' * (len(A[i])//4) + 'BB' * ((len(A[i])%4//2))
    result = '.'.join(A)
  else:
    result = 'AAAA' * (len(A)//4) + 'BB' * ((len(A)%4//2))

  print(result)




