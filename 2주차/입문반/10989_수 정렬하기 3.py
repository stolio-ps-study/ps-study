import sys
input = sys.stdin.readline
print = sys.stdout.write

nums = [0]*10001

for _ in range(int(input())):
    nums[int(input())] += 1

for i, n in enumerate(nums):
    for _ in range(n):
        print(str(i) + '\n')