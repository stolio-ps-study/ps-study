a=input()
second=0

for i in a:
    if i in "ABC":
        second+=3
    elif i in "DEF":
        second+=4
    elif i in "GHI":
        second+=5
    elif i in "JKL":
        second+=6
    elif i in "MNO":
        second+=7
    elif i in "PQRS":
        second+=8
    elif i in "TUV":
        second+=9
    elif i in "WXYZ":
        second+=10
    elif i in "":
        second+=2
    else:
        second+=11

print(second)
