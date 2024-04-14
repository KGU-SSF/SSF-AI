a=int(input("숫자의 개수를 입력하세요"))
list=[] #리스트를 생성
for i in range(a): #입력받은 a만큼 반복
    b=int(input("숫자를 입력하세요"))
    list.append(b)#입력받은 숫자를 리스트에 추가
list.sort() #숫자를 오름차순으로 정렬
print(list)