k=int(input("카드의 갯수를 입력하시오:"))   #첫 번째 줄에 정수k를 입력
list1=[]
total=0 #총합

for i in range(k):
    num=int(input((str(i+1)+"번째 숫자입력:"))) #리스트에 문자열대신 정수로 저장하기 위해 num에 값을 입력받음

    if(num==0):
        total-=list1.pop()  #0일경우 최근에 말한 카드를 지움

    else:
        list1.append(num)   #리스트에 값 추가
        total+=num  #총합 구하기

print("총합:",total)