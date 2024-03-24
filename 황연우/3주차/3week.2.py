#3주차.2번
score=int(input("점수를 입력하시오:"))
if 100>=score>=90:
    print("A")
elif 89>=score>=80:
    print("B")
elif 79>=score>=70:
    print("C")
elif 69>=score>=60:
    print("D")
elif 59>=score>=0:
    print("F")
else:
    print("다시 입력해주세요")
