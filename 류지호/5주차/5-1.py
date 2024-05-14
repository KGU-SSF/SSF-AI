sum=0                                           
name=["준서","이다","홍다","우진","우현"]     #이름 리스트로 하나씩 출력
for i in (name):                             #이름 개수만큼 반복
    while True:                              
        a=int(input(i+"의 성능:"))             #성능을 입력받고 그 값이 0부터 100사이, 5의 배수가 나올떄 까지 반복
        if a>100 or a<0:
            print("0과100사이 입력")
        elif a %5 !=0:
            print("5의 배수 입력")
        else:
            break
    if a<50:                                 #a의 값이 50이 안되면 50으로 저장
        a=50                  
    sum+=a                                    #a의 값을 sum에 더하면서 저장
print('5명의 평균:', sum/5)                     #5명의 평균 출력             
    