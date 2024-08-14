total = 0
people = sorted([int(input()) for _ in range(int(input()))], reverse=True)

for index, i in enumerate(people):
    tip = i - ((index+1) -1)
    if tip > 0 :
        total += tip

print(total)
    
