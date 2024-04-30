#3번문제
sum = 0
for i in range(4):
    a = int(input("num"))
sum += a 

if sum == 1:
     print("A")
elif sum == 2:
     print("B")
elif sum == 3: 
     print("C")
elif sum == 4: 
     print("D")
elif sum == 0: 
     print("E")
else:
     print("다시 입력해주세요")
