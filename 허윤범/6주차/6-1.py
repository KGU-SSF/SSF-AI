def is_palindrome(w):
    return w == w[::-1]

a = ["level", "rotator", "hello"]

for w in a:
    print(is_palindrome(w))