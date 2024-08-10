html = input()

is_tag_opened = False
ans = []
tag = ''
content = ''
for c in html[6:-7]:
    if c == '<':
        tag = '<'
        is_tag_opened = True
    elif c == '>':
        is_tag_opened = False
        if tag.startswith('<div title="'):
            ans.append('title : ' + tag[12:-1])
        elif tag == '</p':
            ans.append(content.strip())
            content = ''
    else:
        if is_tag_opened:
            tag += c
        else:
            if c != ' ' or content[-1:] != ' ':
                content += c

print(*ans, sep='\n')