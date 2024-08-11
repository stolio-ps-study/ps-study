from collections import deque

for _ in range(int(input())):
    p = input()
    input()
    arr = [i for i in input()[1:-1].split(",") if i]
    q = deque(arr)
    is_reversed = True

    for func in p:
        if func == "R":
            is_reversed = not is_reversed
        else:
            if not q:
                print("error")
                break
            if is_reversed:
                q.popleft()
            else:
                q.pop()
    else:
        if not is_reversed:
            q.reverse()
        print('['+','.join(q)+']')