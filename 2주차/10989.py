'''
import sys
input = sys.stdin.readline
N=int(input())
my_list=[]
for i in range(N) :
    s= int(input())
    my_list.append(s)
set(my_list)
my_list.sort()
for i in list(my_list):
    print(i)
'''
## 메모리 초과
N = int(input())
count=[0 for _ in range(10001)]
for i in range(N):
    s= int(input())
    count[s]+=1

for j in range(10001):
    if count[j]!=0 :
        pass  ##