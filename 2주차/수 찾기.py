import sys

n = int(sys.stdin.readline().strip())
numbers = set(map(int, input().split()))  

m = int(sys.stdin.readline().strip())
question = list(map(int, input().split()))

for i in question:
    if i in numbers:
        print(1)
    else:
        print(0)
