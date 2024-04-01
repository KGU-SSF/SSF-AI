sclist = []

for i in range (5):
    usinput = int(input("입력하시오: "))
    if usinput >= 50:
        sclist.append(input)
    elif usinput < 50:
        sclist.append(50)

avg = sum(sclist)/len(sclist)
print(avg)