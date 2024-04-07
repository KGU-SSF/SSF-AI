sum = 0
for i in range(5):
    g = int(input("성적: "))
    if g < 50:
        g = 50
    sum += g
    
print(sum/5)
