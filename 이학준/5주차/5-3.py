import random
dbc = [0, 0, 0, 0, 1, 1, 1, 1] 
total = []#한 번에 출력하기 위해 list를 사용함
for i in range(0,3,1):
    num=0 #num은 list에 넣기 전 총합을 구하기 위해 사용
    dbcejswla = random.sample(dbc, 4)#경우의 수 생성
    print(dbcejswla)
    for j in range(0,4,1):#생성된 경우의 수를 돌면서(to be continue)
        num=num+dbcejswla[j]#총합 계산
    total.append(num)#append는 list에 추가하는 함수
#

for i in range(0,3,1):
    if(total[i]==0):
        print("D")
    elif(total[i]==1):
        print("C")
    elif(total[i]==2):
        print("B")
    elif(total[i]==3):
        print("A")
    elif(total[i]==4):
        print("E")