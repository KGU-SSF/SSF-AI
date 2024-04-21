word = input('단어를 입력하세요 : ')
palindrome = False

if (word == word[::-1]) :
  palindrome = True

else :
  palindrome = False

print(palindrome)
