w = input("world : ")

is_palindrome = True
for i in range(len(w) // 2):
    if w[i] != w[-1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("회문 입니다.")
else:
    print("회문이 아닙니다.") 
