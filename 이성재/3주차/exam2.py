def score(n):
    if (n >= 100 or n <= 0):
        print("다시 입력해주세요")
    elif (n >= 90):
        print("A")
    elif (n >= 80):
        print("B")
    elif (n >= 70):
        print("C")
    elif (n >= 60):
        print("D")
    else:
        print("F")
        
numbers= int(input())
score(numbers)