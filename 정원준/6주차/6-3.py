a=int(input("숫자의 개수를 입력하세요"))
list=[]
for i in range(a):
    b=int(input("숫자를 입력하세요"))
    list.append(b)
list.sort() #숫자를 오름차순으로 정렬
print(list)