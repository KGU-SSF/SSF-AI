num=[]
N=int(input("몇개의 숫자를 입력할 것인지 알려주세요"))
for  i in range(N):
    a= int(input())
    
    if a!=0 :
        num.append(a)
    else:
        num.pop()
        
print(sum(num))