#3
a = int(input("총 입력할 수의 갯수를 적으세요: "))
b = []

for i in range(a):
    c = int(input("수: "))
    b.append(c)
    
b.sort()

for i in range(a):
    print(b[i])
    
    


    