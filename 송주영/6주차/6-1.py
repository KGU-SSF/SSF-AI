a = input("단어를 입력 하시오: ")

if a == a[::-1]: #원래 단어 == 뒤집은 단어
    print("true")
else:
    print("False")