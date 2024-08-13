#1181
#단어와 길이를 딕셔너리에 저장
#17분

N=int(input())
dic={}

for _ in range(N):
  word=input()
  dic[word]=len(word)

values= set(list(dic.values()))
value_list= list(values)
value_list.sort()

sort_word=[]

for i in range(len(value_list)):
  sword= [k for k,v in dic.items() if v == value_list[i]]
  if len(sword) > 1:
    sword.sort()
    for j in range(0,len(sword)):
      sort_word.append(sword[j])
  elif len(sword) == 1:
    sort_word.append(sword[0])


for i in range(len(sort_word)):
  print("%s"%sort_word[i])

