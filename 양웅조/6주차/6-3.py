a = int(input("몇 개의 숫자를 입력할까요"))
happy = []
for x in range (1,a+1) :
    b = int(input("숫자를 입력하세요"))
    happy.append(b)

happy.sort() #정렬해주는 sort 사용
print (happy)