# 1920_수 찾기
import sys

n=int(sys.stdin.readline())
nn=set(map(int, sys.stdin.readline().strip().split()))

m=int(sys.stdin.readline())
mm=list(map(int, sys.stdin.readline().strip().split()))

for num in mm:
    print(1) if num in nn else print(0)