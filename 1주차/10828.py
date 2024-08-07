n=int(input())
stk=[]

for _ in range(n):
    s = input().strip()
    if s.startswith('push'):
        stk.append(int(s.split()[1]))
    elif s=='top':
        if stk:
            print(stk[-1])
        else:
            print(-1)
    elif s=='pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif s=='size':
        print(len(stk))
    elif s=='empty':
        if stk:
            print(0)
        else:
            print(1)
    
    