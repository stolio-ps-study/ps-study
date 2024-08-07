n=int(input())
arr=[]
for _ in range(n):
    w, h = map(int,input().split())
    arr.append((w,h))

for i in arr:
    rank=1
    for j in arr:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    # 한 줄로 출력하기 위해서 end=" " 사용
    print(rank, end=" ")