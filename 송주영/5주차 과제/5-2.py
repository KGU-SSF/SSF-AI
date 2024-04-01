a = int(input("숫자를 입력하시오: "))

def star(k):
    for i in range(1, k+1):
        spaces = " " * (a - i)  
        stars = "*" * (2*i - 1)
        print(spaces + stars)

for i in range(1, a+1):
    star(i)