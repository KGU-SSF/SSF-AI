def star_sort(N):   #별 오른쪽 으로 정렬
    for i in range(1, n + 1):
        space = " " * (n - i) 
        star = "*" * i  
        print(space + star)


n = int(input("숫자를 입력하세요: "))
star_sort(n)
