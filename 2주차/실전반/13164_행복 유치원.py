n, k = map(int, input().split())
arr = list(map(int, input().split()))
diff = sorted(arr[i] - arr[i-1] for i in range(1, len(arr)))

print(sum(diff[:n-k]))