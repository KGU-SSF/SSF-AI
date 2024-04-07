def pyramid(jul):
    for i in range(1, jul + 1):
        spaces = jul - i
        print(" " * spaces + "* " * i) #별과 별사이의 간격은 "*"*i 할때 저절로 띄어지는거 이용

jul = int(input("줄 수 입력: "))
pyramid(jul)