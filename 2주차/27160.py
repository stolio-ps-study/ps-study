n=int(input())
straw=0
banana=0
lime=0
plum=0

for _ in range(n):
    s, cnt=input().split()
    if s=='STRAWBERRY':
        straw+=int(cnt)
    elif s=='BANANA':
        banana+=int(cnt)
    elif s=='LIME':
        lime+=int(cnt)
    else:
        plum+=int(cnt)

if straw==5 or banana==5 or lime==5 or plum ==5:
    print("YES")
else:
    print("NO")