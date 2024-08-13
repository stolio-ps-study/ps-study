ans = input().replace('XXXX', 'AAAA').replace('XX', 'BB')
print(ans if 'X' not in ans else -1)