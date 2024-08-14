N = int(input())  # 사람 수 입력

size = []  # 몸무게, 키 저장

for k in range(N):
    x, y = map(int, input().split())
    size.append((x, y))

n = int(input())

size = []
rank = []
for i in range(n):
    a, b = map(int, input().split())
    size.append((a, b))

for i in range(n):
    count = 0
    for j in range(n):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            count += 1
    rank.append(count + 1)

for d in rank:
    print(d, end=" ")
