grade = int(input("점수를 입력하세요.\n"))
    
if 90 <= grade <= 100 :
    print("A")
    
elif 80 <= grade < 90 :
    print("B")
    
elif 70 <= grade < 80 :
    print("C")
    
elif 60 <= grade < 70 :
    print("D")
    
elif grade > 100 :
    print("다시 입력해주세요.")
    
elif grade < 0 :
    print("다시 입력해주세요.")

else :
    print("F")
