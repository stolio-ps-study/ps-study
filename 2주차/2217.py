# 2217 로프

n=int(input())
w=[int(input()) for _ in range(n)]

w.sort(reverse=True)
res = [w[i]*(i+1) for i in range(n)]

print(max(res))