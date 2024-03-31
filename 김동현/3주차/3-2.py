score = int(input())
while (score < 0) | (score > 100):
    print("다시 입력해주세요")
    score = int(input())
if (score >= 90)&(score <= 100):
    print("A")
elif (score >= 80)&(score <= 89):
    print("B")
elif (score >= 70)&(score <= 79):
    print("C")
elif (score >= 60)&(score <= 69):
    print("D")
else:
    print("F")
    #commit 메세지 수정용