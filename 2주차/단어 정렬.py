words = set()

for _ in range(int(input())):
    word = input()
    words.add(word)

def sort_key(word):
    return (len(word), word)

sorted_words = sorted(words, key=sort_key)

for word in sorted_words:
    print(word)
