nums = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ans = 0

for c in input():
    for i, string in enumerate(nums):
        if c in string:
            ans += i

print(ans)
