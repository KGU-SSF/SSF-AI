student=[0,0,0,0,0]
sum=0
for i in range(5):
    student[i]=int(input())
    if student[i]<50:
     student[i]=50
    sum=sum+student[i]       

print(sum/5)
