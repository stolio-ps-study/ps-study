N = int(input())
tip= [int(input()) for _ in range(N)]
tip.sort(reverse=True)
realtip=0
total=0
for i in range(N):
    realtip=tip[i]-(i+1-1)
    if realtip <0 :
        continue
    total+=realtip

print(total)
## 5분