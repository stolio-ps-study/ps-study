from sys import stdin

input = stdin.readline

stack = []

for instruction in (input().strip().split() for _ in range(int(input()))):
    if instruction[0] == 'push':
        stack.append(instruction[1])
    elif instruction[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif instruction[0] == 'size':
        print(len(stack))
    elif instruction[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
