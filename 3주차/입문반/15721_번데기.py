a = int(input())
t = int(input())
s = input()

cnt, tmp = 0, 4
while cnt + tmp < t:
    cnt += tmp
    tmp += 1

t -= cnt
cnt *= 2
if t == 1:
    cnt += 1 + int(s)
elif t == 2:
    cnt += 3 + int(s)
else:
    if s == '0':
        cnt += 2 + t
    else:
        cnt += tmp + t

print((cnt - 1) % a)
