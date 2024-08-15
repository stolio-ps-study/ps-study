str=input()
arr=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt=0

for a in arr:
    str=str.replace(a,'0')

print(len(str))