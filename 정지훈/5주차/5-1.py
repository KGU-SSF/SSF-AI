sum = 0

for i in range(5):
    a = int(input())

    if a % 5 != 0:
        print("점수를 잘못 입력 했습니다.")
        break

    if a< 50:
        a = 50
    
    sum += a
    
average = int(sum / 5)     

print(average)