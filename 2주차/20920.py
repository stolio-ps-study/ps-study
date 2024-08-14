N,M = map(int,input().split())
word =[input() for _ in range(N)]
for w in word :
    if len(w) < M :
        word.remove(w)
count={x:word.count(x) for x in word}
word.sort(key=count)
'''
for i in count.keys():
    if i == i-1 :
        if len(i)>len(i-1):
'''