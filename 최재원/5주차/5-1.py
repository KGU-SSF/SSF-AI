student = 5
score = []
sum = 0

for i in range(student):
    input_score = int(input("성적을 입력하세요. : "))
    
    if(input_score < 50):
        sum += 50
    else:
        sum += input_score
        
    
avg = sum /5
print(avg)
