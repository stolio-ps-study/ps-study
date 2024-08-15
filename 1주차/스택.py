def push(X):
    my_stack.append(X)

def top():
    if len(my_stack) >= 1:
        return my_stack[-1]
    else:
        return -1

def size():
    return len(my_stack)

def empty():
    if len(my_stack) == 0:
        return 1
    else:
        return 0

def pop():
    if len(my_stack) == 0:
        return -1
    else:
        return my_stack.pop()

my_stack = []
number = int(input())
commands = [input() for _ in range(number)]

for order in commands:
    under = order.split()
    if under[0] == 'push':
        push(int(under[1]))
    elif under[0] == 'top':
        print(top())
    elif under[0] == 'size':
        print(size())
    elif under[0] == 'pop':
        print(pop())
    elif under[0] == 'empty':
        print(empty())
