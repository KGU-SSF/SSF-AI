arr=[]
for i in range(0,3,1):
    arr.append(input("숫자를 입력하세요 :"))

for i in range(0,3,1):
    a,b,c,d = map(int,arr[i].split())
    total= a + b + c + d
    if total==0:
      print("E")
    elif total==1:
        print("C")
    elif total==2:
        print("B")
    elif total==3:
        print("A")
    elif total==4:
        print("D")