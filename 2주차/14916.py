#14916_거스름돈

n=int(input())
cnt=0

while True:
    if n%5==0:
        cnt+=n//5 # 5원으로 나눌 수 있는 동전 개수
        break
    else:
        n-=2
        cnt+=1


if n<0:
    print(-1)
else:
    print(cnt)