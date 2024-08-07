a = input()
time=0  # time은 0으로 초기화
letter=["ABC","DEF","GHI","JKL",
      "MNO","PQRS","TUV","WXYZ"]  # 리스트에 나눠서 저장
for i in a:  # 각 글자마다 반복
    for num,l in enumerate(letter):  # letter 리스트의 내용을 인덱스와 같이 반복
        if i in l :                  # 만약 글자가 letter 안에 있다면, time에 각 시간을 더한다.
            time+=(num+3)            # (num +3) 처음 ABC 가 3초 걸림

print(time)

"""
a= input()
time=0
for i in a:
    if i in "ABC":
        time+=3
    elif i in "DEF":
        time+=4
    elif i in "GHI":
        time+=5
    elif i in "JKL":
        time+=6
    elif i in "MNO":
        time+=7
    elif i in "PQRS":
        time+=8
    elif i in "TUV":
        time+=9
    elif i in "WXYZ":
        time+=10
    else :
        time+=11
"""