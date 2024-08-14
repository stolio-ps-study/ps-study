n = int(input())
coin =0
while( n > 0 ) :

    if n%5==0 :  ## 5의 배수
        coin += n//5
        break
    else :  ## 5의 배수가 아닐때
        n-=2
        coin +=1
if n<0 :
    print(-1)
else :
    print(coin)