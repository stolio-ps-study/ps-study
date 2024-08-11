K = int(input()) #정수 K
number = [] # 

for _ in range(K):
    num = int(input())
    if num == 0:
        if number:
            number.pop()
    else:
        number.append(num)

print(sum(number))
