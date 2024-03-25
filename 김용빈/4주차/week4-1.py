def star_sort(N):
    for i in range(1, n + 1):
        space = " " * (n - i) 
        star = "*" * i  
        print(space + star)


n = int(input("숫자를 입력하세요: "))
star_sort(n)
