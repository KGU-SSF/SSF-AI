score = int(input())

if (score > 100 or score < 0):
    print("다시 입력해주세요")
elif (score >= 60):
    if (score >= 70):
        if (score >= 80):
            if (score >= 90):
                print("A")
            else:
                print("B")
        else:
            print("C")
    else:
        print("D")

else:
    print("F")