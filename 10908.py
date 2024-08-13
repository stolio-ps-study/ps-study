#10908
#메모리 초과

N = int(input())
if N <= 100000000 :
  nlist = [int(input()) for _ in range(N)]

nlist.sort()



for i in nlist:
    print(i)


