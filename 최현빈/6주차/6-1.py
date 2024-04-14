word = input("단어를 입력하시오: ")
is_palindrome = True
for i in range(len(word)//2):
    if word[i] != word[-1 - i]:
        is_palindrome = False
print(is_palindrome)