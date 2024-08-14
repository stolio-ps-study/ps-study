N,K = map(int,input().split())
money=[]
for _ in range(N):
    money.append(int(input()))
coin=0
money.sort(reverse=True)
for i in money:
    if K>=i :
        coin+= K//i
        K%=i

print(coin)


