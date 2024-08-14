## 5분
S = input()

S=S.replace("XXXX","AAAA")
S=S.replace("XX","BB")

if S.count("X")!=0 :
    print(-1)
else:
    print(S)