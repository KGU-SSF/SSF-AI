
a=input("문자를 입력하세요")
word=[]
for char in a:
    word.extend(a)
re_word=word[::-1]
if word==re_word:
    print("True")
else:
    print("False")