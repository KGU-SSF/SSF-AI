sum = 0

for i in range(5):
    a= int(input())
    
    if(a<0 or a>100) :
        print("성능은 0점이상, 100점 이하여야 합니다.")
        break
    if(a%5 != 0):
        print("성능을 5의 배수로 입력해야합니다.")
        break
    
    if(a<50) :
        a = 50
        
    sum += a
average = int(sum/5)

print(average)