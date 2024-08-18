from sys import stdin
input = stdin.readline

arr = [int(input()) for _ in range(int(input()))]
arr.sort(reverse=True)

ans = 0
for i in range(len(arr)):
    if arr[i]-i <= 0:
        break
    ans += arr[i]-i
print(ans)