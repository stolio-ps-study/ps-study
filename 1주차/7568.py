N = int(input())  # 사람 수 입력

size = []  # 몸무게, 키 저장

for k in range(N):
    x, y = map(int, input().split())
    size.append((x, y))