def selfNumber(n):
    my_list = []
    number = str(n)
    for i in number:
        my_list.append(int(i))
    return n + sum(my_list)

i, j = 1,1
new_list = [] 

while i < 10000 and j < 10000 :
    result = selfNumber(i)
    new_list.append(result) 
    i += 1 
    if j not in new_list:
        print(j)
    j += 1 

