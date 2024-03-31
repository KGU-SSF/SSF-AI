test = int(input())

if test>=0 and test<=100:
    if test>=90:
        print('A')
    elif test>=80:
        print('B')
    elif test>=70:
        print('C')
    elif test>=60:
        print('D')
    else:
        print("F")
else:
    print("다시 입력해주세요")
    