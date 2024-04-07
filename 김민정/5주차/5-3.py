yut1= input().split()
yut2= input().split()
yut3= input().split()
yut4=input().split()

count_back = sum([yut1.count('0'),yut2.count('0'),yut3.count('0'),yut4.count('0')])

if count_back == 0:
    print("E")
elif count_back ==1:
    print("A")
elif count_back ==2:
    print("B")
elif count_back ==3:
    print("C")
else:
    print("D")