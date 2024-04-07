성능 = []
for i in range(5):
    성능.append(int(input("성능을 입력하세요.")))
결과 = []
for i in 성능:
    if i < 50:
        결과.append(50)
    else : 결과.append(i)
    
a=sum(결과)/len(결과)
print("평균 : ",int(a))