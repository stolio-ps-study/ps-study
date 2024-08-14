import sys

number = list(map(int, sys.stdin.readline().split()))

word_count = {}

for _ in range(number[0]):
    word = sys.stdin.readline().strip()
    if len(word) >= number[1]:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

def sort_key(word):
    return (-word_count[word], -len(word), word)

sorted_words = sorted(word_count.keys(), key=sort_key)

for word in sorted_words:
    print(word)
