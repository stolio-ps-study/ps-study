arr = [tuple(map(int, input().split())) for _ in range(int(input()))]


def find_rank(t):
    ans = 1
    for x, y in arr:
        if x > t[0] and y > t[1]:
            ans += 1
    return ans


print(*(find_rank(i) for i in arr))
