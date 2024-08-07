K = int(input())  # 숫자 개수 입력받기
a=[]  # 수를 저장할 리스트
for i in range(K):
    num=int(input())  # 숫자 입력
    a.append(num)  # 리스트에 추가
    if (num ==0):  # 만약 숫자가 0 이라면 가장 최근의 수를 지워야하므로
        a.pop()    # 현재 0 과 그 전 숫자를 지운다
        a.pop()

print(sum(a))