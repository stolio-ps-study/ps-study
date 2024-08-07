word = input()
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for alphabet in alphabets:
    while alphabet in word:
        word = word.replace(alphabet, ' ', 1) 
        count += 1

count += len(word.replace(' ', ''))

print(count)
