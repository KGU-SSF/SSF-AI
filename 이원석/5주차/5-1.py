s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
score=0
std = [s1, s2, s3, s4, s5]
for i in std:
    std[i] = int(input("성능을 입력하세요: "))
    if (std[i]<50):
        std[i]=50
    score = score + std[i]

print(score/5)

