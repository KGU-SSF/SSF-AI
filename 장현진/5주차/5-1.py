grade=[]
for i in range(5):
   grade.append(int(input("성능을 입력하세요:")))
result=[]
for i in grade:
    if i<50:
        result.append(50)
    else:
     result.append(i)

average=sum(result)/len(result)
print("평균:",int(average))