# 스택 = last in first out
import sys  ## 시간 초과떠서 readline 추가
input = sys.stdin.readline
stk = []  # 리스트로 스택 변수 만들기
N = int(input())  # 명령 개수 받기
for i in range(N):
    order = input().split()  # 띄어쓰기 기준으로 리스트 생성
    if order[0] == "push":
        stk.append(order[1])
    elif order[0] == "pop":
        if len(stk) == 0:
            print(-1)
        else :
            a=stk.pop()
            print(a)
    elif order[0] == "size":
        print(len(stk))
    elif order[0] == "empty":
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "top":
        if len(stk) == 0:
            print(-1)
        else :
            print(stk[-1])