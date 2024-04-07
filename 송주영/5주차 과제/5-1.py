sclist = [] #리스트 생성

for i in range (5):
    usinput = int(input("입력하시오: "))
    if usinput >= 50: #입력한 수와 50 사이간의 대소관계확인(클때)
        sclist.append(input) #입력
    elif usinput < 50: #작을때
        sclist.append(50) #50으로 입력

avg = sum(sclist)/len(sclist)
print(avg)