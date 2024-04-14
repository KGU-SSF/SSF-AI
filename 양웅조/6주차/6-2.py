import random
cardlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
picklist = [] #뽑은 카드를 저장하기 위한 빈 리스트 생성
a = int(input("몇 개의 카드를 뽑을까요"))
for x in range (1,a+1) :
    b = int (input("0-9중 카드숫자입력"))
    picklist.append(b) #입력 값을 리스트에 추가하기 위해 씀
    if b == 0 :
        del picklist[x-2] #만약 0이 나왔을 때 그 전의 원소를 삭제하기 위해 씀

result = sum(picklist)

print (result)




