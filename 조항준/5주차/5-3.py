
def check(bae,deung) :
    if(bae == 1 and deung == 3):
        print("A")
    elif(bae == 2 and deung == 2):
        print("B")
    elif(bae == 3 and deung == 1):
        print("C")
    elif(bae == 4 and deung == 0):
        print("D")
    elif(bae == 0 and deung == 4):
        print("E")
    
data1 = [0,1,0,1]
data2 = [1,1,1,0]
data3 = [0,0,1,1]

check(data1.count(0), data1.count(1))
check(data2.count(0), data2.count(1))
check(data3.count(0), data3.count(1))