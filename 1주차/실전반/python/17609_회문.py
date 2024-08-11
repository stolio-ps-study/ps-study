def is_palindrome(s, front, end, flag):

    while front < end:
        if s[front] != s[end]:
            if flag:
                return 1
            else:
                return (is_palindrome(s, front+1, end, True) and is_palindrome(s, front, end-1, True)) +1
        front += 1
        end -= 1
    return 0


for _ in range(int(input())):
    s = input()
    print(is_palindrome(s, 0, len(s)-1, False))