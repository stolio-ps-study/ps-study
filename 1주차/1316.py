n=int(input())
cnt=n

for _ in range (n):
    str=input()
    for i in range(len(str)-1):
        if str[i]==str[i+1]:
            continue
        elif str[i] in str[i+1:]:
            cnt-=1
            break

print(cnt)