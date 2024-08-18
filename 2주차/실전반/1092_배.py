input()
cranes = list(sorted(map(int, input().split()), reverse=True))
input()
boxes = list(sorted(map(int, input().split()), reverse=True))


if cranes[0] < boxes[0]:
    print(-1)
else:
    cnt = 0
    while boxes:
        i = 0
        for crane in cranes:
            if not boxes or crane < boxes[-1]:
                break
            while i < len(boxes) and crane < boxes[i]:
                i += 1
            boxes.pop(i)
        cnt += 1
    print(cnt)