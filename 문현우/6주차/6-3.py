""" 정렬의 종류
    1.선택정렬:여러 데이터중 가장 작은 데이터를 선택해 앞의 데이터와 바꾸는 정렬
    =>단점:매우 비효율적이다 ->올바로 정렬되어있을때도 다 첨부터 끝까지 확인하기 떄문에 시간이 매우 많이 소요된다
    2.삽입 정렬:데이터를 하나씩 확인하고 적절한 위치에 삽입
    ->데이터가 적절한 위치에 들어가기전에 !!그앞까지의 데이터가 맞다고(정렬되어 있다) 가정!!
    =>장점:데이터가 거의 정렬되어 있을때 매우 유리!! 선택정렬과 반대 느낌
    3.퀵정렬:피버(리스트[0])을 기준으로 크면 오른쪽 작으면 왼쪽으로 보내다가 더이상 보낼게 없을때(맞물리면)
    맞물린 수중 작은수를 피버와 교환(작은수가 피버가 되고 )피벗을 기준으로 앞뒤로 다시 반복
    =>장점:운이 좋게 피벗을 잘고르게되면 O(N*logB=N) 이지만 
     단점:피벗을 잘못골라 피벗이 작다면 O(n*n 즉N^2가 된다)
"""
N=int(input("몇개를 입력할건지 쓰시오:"))
number=[]
for _ in range(N):
    number.append(int(input()))
no_repetition=list(set(number)) #반복되지 않는 수 리스트 set사용
'''for i in range(len(no_repetition)):
    min_id=i
    if i == len(no_repetition)-1:
        break
    for j in range(i+1,len(no_repetition)) :
        if no_repetition[min_id]>no_repetition[j]:
            min_id=j
    no_repetition[i],no_repetition[min_id]=no_repetition[min_id],no_repetition[i]
'''
no_repetition.sort() #sort하나면 위에 다 생략가능..
print(no_repetition)
        



    