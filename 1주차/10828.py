#10828
"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다. 

"""

def push(list,x):
  list.append(x)

def pop(list):
  if len(list)!=0:
    result=list[-1]
    list.pop()
    return result

  else:
    return -1
  
def size(list):
  return len(list)

def empty(list):
  if len(list) ==0:
    return 1
  else:
    return 0

def top(list):
  if len(list) !=0:
    return list[-1]
  else:
    return -1

num=int(input())

list=[]
for i in range(num):
  inputs = input().split()
  if len(inputs) == 2:
    order, n = inputs
    num=int(n)
  else:
    order= inputs[0]
    n = None

  if order == 'push':
    push(list,num)
  elif order == 'pop':
    result=pop(list)
    print(result)
  elif order == 'size':
    result=size(list)
    print(result)
  elif order == 'empty':
    result=empty(list)
    print(result)
  elif order == 'top':
    result=top(list)
    print(result)
