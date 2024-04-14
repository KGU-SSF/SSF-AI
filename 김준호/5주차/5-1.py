sum=0
for i in range (5):
    n = int(input())
    if n % 5 !=0 or n<0 or n>100:
        n = int(input("5의 배수인 0~100만 입력가능:"))
    if n<50:
        n = 50
    sum += n
print(sum/5)