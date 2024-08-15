import sys

# 숫자의 범위가 1부터 10000까지이므로, 크기가 10001인 리스트를 생성
count = [0] * 10001

# 첫째 줄에서 N 값을 입력받음
n = int(sys.stdin.readline())

# N개의 수를 입력받아 해당 수의 개수를 count 배열에 기록
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

# count 배열을 순회하며, 각 숫자를 개수만큼 출력
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
