score = []
avr = 0

for i in range(5):
    score.append(int(input()))
    
    if (score[i] < 50):
        score[i] = 50
    avr += score[i]
    
avr /= 5

print(int(avr))