#6주차 2번

k = int(input("숫자를 입력하시오. : "))    #값입력
li = []     #값을 입력받을 수 있는 리스트 생성
for i in range(k):
    n = int(input())    #k번만큼 n을 입력받기
    if(n==0):
        li.pop()    #n이 0이면 리스트에 있는 값을 제거
    
    else:
            li.append(n)    #입력받은 값이 0이 아니면 리스트에 n값을 추가
print(sum(li))  #리스트에 합을 구해 출력