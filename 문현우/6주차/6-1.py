#1.절반으로 나눠서 앞뒤 비교!

word=input("영어로 입력(회문인지 확인):")
length=len(word) 
for i in range (length //2):
    if word[i]==word[length-1-i]:
        print("True")
        break
    else:
        print("False")
        break

""" #2.reversed()사용!
word = input("영어로 입력(회문인지 확인):")
reversed_word =''.join(reversed(word))
if word == reversed_word:
    print("True")
else:
    print("False")
#여기서 reversed_word = ''.join(reversed(word))를 한번 더쓰는 이유는
#reversed(word)를 쓰면 iterator(반복 가능한 객체)로 반환되기 때문에 join을 써서 객체를 붙여 문자열로 만들어야한다
#이때 join앞에 ''를 쓰는거는  ['h' 'e' 'l' 'l' 'o'] 이런식으로 구분되어 있는거를 합치기 위해서이다
# ''.을 안쓰면 에러가 나온다
"""