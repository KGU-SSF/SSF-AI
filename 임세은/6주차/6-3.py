N=int(input("입력받을 갯수는?"))
list1=[]

for i in range(N):
    num=int(input("숫자입력:")) #리스트에 문자열대신 정수로 저장하기 위해 num에 값을 입력받음
    list1.append(num)   #리스트에 값 추가

list1.sort()

print(list1)