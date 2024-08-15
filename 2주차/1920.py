import sys
input = sys.stdin.readline
N = int(input())
n1 = set(input().split())
M = int(input())
n2 = input().split()
for i in n2 :
    if i in n1 :
        print(1)
    else:
        print(0)