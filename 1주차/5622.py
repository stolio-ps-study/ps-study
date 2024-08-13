#5622
##걸린 시간 = 다이얼 숫자+1

A=input("")
B=list(A)
num=0
sum=0
for i in range(0,len(B)):
  if (ord(B[i])>= ord('A') and ord(B[i])<=ord('C')):
    num=3
  elif (ord(B[i])>= ord('D') and ord(B[i])<=ord('F')):
    num=4
  elif (ord(B[i])>= ord('G') and ord(B[i])<=ord('I')):
    num=5
  elif (ord(B[i])>= ord('J') and ord(B[i])<=ord('L')):
    num=6
  elif (ord(B[i])>= ord('M') and ord(B[i])<=ord('O')):
    num=7
  elif (ord(B[i])>= ord('P') and ord(B[i])<=ord('S')):
    num=8
  elif (ord(B[i])>= ord('T') and ord(B[i])<=ord('V')):
    num=9
  elif (ord(B[i])>= ord('W') and ord(B[i])<=ord('Z')):
    num=10

  sum+=num

print(sum)