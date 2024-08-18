n, k = map(int, input().split())
nums = input()

ans = []

for num in nums:
    while k and ans and num > ans[-1]:
        ans.pop()
        k -= 1
    ans.append(num)

print(''.join(ans[:-k] if k else ans))