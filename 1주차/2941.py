word = input()
count = 0

for i in range(len(word)):
    if i < len(word):
        if word[i] == "c":
            if word[i+1] == "=":
                count += 1
                i += 2
            elif word[i+1] == "-":
                count += 1
                i += 2
        if word[i] == "d":
            if word[i+1] == "-":
                count += 1
                i += 2
            elif word[i+1]=="z":
                if word[i+2]=="=":
                    count += 1
                    i += 3
        if word[i] == "l":
            if word[i+1] == "j":
                count += 1
                i += 2
        if word[i] == "n":
            if word[i+1] == "j":
                count += 1
                i += 2
        if word[i] == "s":
            if word[i+1] == "=":
                count += 1
                i += 2
        if word[i] == "z":
            if word[i+1] == "=":
                count += 1
                i += 2
        else:
            count += 1
    else:
        break
print(count)
