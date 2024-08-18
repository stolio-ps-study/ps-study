import sys
from collections import Counter
input = sys.stdin.readline


def get_counter(arr):
    sums = [0]
    for num in arr:
        sums.append(sums[-1] + num)
    for i in range(len(arr)-1):
        num = arr[i]
        sums += list(map(lambda x: x-num, sums[-(len(arr)-i-1):]))
    return Counter(sums[1:])


t = int(input())
input()
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))

a_counter = get_counter(a)
b_counter = get_counter(b)

ans = 0
for i in a_counter:
    if t-i in b_counter:
        ans += a_counter[i] * b_counter[t-i]
print(ans)