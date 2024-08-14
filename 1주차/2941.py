s = input()
letter = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
i = 0  # 현재 인덱스 위치
tmp = 0  # 알파벳 수

while i < len(s):
    if s[i:i+3] in letter:  #3글자를 보고 letter 안의 글자라면
        i += 3              #현재 인덱스 위치를 그 3글자 뒤로 바꾼다
    elif s[i:i+2] in letter:
        i += 2
    else:
        i += 1
    tmp += 1

print(tmp)
