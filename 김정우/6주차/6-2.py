a = int(input("정수를 입력하시오 : "))
c = []
for i in range(0,a):
    b = int(input())
    if b<10 and b>0 :
        c.append(b)
    else :
        c.pop()
print("숫자의 합 : ",sum(c))
