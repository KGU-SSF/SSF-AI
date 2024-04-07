a = int(input("숫자를 입력하시오: ")) #숫자 입력

def star(k): #함수입력
    for i in range(1, k+1):
        spaces = " " * (a - i)  #입력 된수에서 마이너스*빈칸
        stars = "*" * (2*i - 1) # 별을 차례대로 개수를 늘려가며 제출
        print(spaces + stars)

for i in range(1, a+1):
    star(i)