#2
score=(int(input("시험점수를 입력하세요:")))

if score>100 or score<0:
    print("다시입력해주세요")
elif 100>=score>=90:
    print("A")
elif 89>=score>=80:
    print("B")
elif 79>=score>=70:
    print("C")
elif 69>=score>=60:
    print("D")
else:
    print("F")