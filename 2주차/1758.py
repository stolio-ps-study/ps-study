# 1758_알바생 강호

n=int(input())
arr=[]
tip=0

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n):
    t=arr[i]-i
    if t>0:
        tip+=t

print(tip)