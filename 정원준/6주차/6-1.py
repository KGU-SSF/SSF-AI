a=input("단어를 입력하세요") 
if a==a[::-1]: #단어를 뒤집어서 판별
    print("True")
else:
    print("False")