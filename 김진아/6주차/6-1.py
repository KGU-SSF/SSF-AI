word = input("단어를 입력하시오 : ")

if word == word[::-1]: 
    print("True")
else:
    print("False")