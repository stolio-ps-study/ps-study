a, b, c, d, e, f = map(int, input().split())
x = (b * f - c * e) // (b * d - a * e)
y = (a * f - c * d) // (a * e - b * d)
print(x, y)
