import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    files = list(map(int, input().split()))
    heapq.heapify(files)
    ans = 0
    while len(files) > 1:
        tmp_file = heapq.heappop(files) + heapq.heappop(files)
        ans += tmp_file
        heapq.heappush(files, tmp_file)
    print(ans)

