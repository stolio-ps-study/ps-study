import sys

n=int(sys.stdin.readline())

# strip()를 써서 뒤에 공백 없애주기
arr=[sys.stdin.readline().strip() for _ in range(n)]

# 중복 요소 제거를 위해 set 사용
arr=list(set(arr))
arr.sort()
# 길이를 기준으로 정렬
arr.sort(key=len)

for i in arr:
    print(i)