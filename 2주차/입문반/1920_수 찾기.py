input()
nums = set(input().split())

input()
print(*(int(i in nums) for i in input().split()), sep='\n')
