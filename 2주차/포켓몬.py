import sys

input_list = sys.stdin.readline().strip().split()
n, m = int(input_list[0]), int(input_list[1])

book = [sys.stdin.readline().strip() for _ in range(n)]
book_dict = {book[i]: i for i in range(n)}

for _ in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(book[int(question) - 1])
    else:
        print(book_dict[question] + 1)
