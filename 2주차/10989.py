import sys

n=int(sys.stdin.readline())
cnt = [0]*10001

for i in range(n):
    x=int(sys.stdin.readline())
    cnt[x]+=1

for i in range(len(cnt)):
    if cnt[i]!=0:
        for _ in range(cnt[i]):
            print(i)