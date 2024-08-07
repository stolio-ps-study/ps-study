number = int(input())
my_list = []

for i in range(number):
    n = int(input())
    if n == 0 and len(my_list) > 0:
        my_list.pop()  # 마지막 요소를 제거 (이전 입력값)
    else:
        my_list.append(n)

total = sum(my_list)
print(total)
