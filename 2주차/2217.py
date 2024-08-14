N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)  ## 내림차순

max= 0
for i in range(N):
    weight = rope[i] * (i+1)  # 최대 중량
    if weight > max:
        max = weight

print(max)
