n=5
list1=[]
result=0

#list1 리스트에 for문을 통해 값을 5번 입력받음
for i in range(n):
    num=int(input("숫자입력:")) #리스트에 문자열대신 정수로 저장하기 위해 num에 값을 입력받음
    list1.append(num)   #리스트에 값 추가

for i in range(n):    
    if list1[i] <50:    #점수가 50보다 작을시
        list1[i]=50 #점수가 50이하일때 리스트에 50을 저장함
    result+=list1[i]    #총점

average=result//n   #평균을 정수형으로 변환
print("평균:",average)