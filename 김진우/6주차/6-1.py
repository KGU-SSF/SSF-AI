a = input('단어 : ')
 
is_palindrome = True                 
for i in range(len(a) // 2):      
    if a[i] != a[-1 - i]:      
        is_palindrome = False        
        break
 
print(is_palindrome)                 
 