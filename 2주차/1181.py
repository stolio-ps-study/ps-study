N = int(input())
my_list=[]
for i in range(N):
    my_list.append(input())
my_list=list(set(my_list))
my_list.sort()
my_list.sort(key=len)
for j in my_list:
    print(j)