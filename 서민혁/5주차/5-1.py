list = []
sum = 0
for i in range(0,5):
    list.append(int(input()))
for i in range(0, 5):
    if(list[i]<50):
        sum += 50
    else:
        sum += list[i]
print(sum/5)