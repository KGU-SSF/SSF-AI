a = int(input("몇개의 숫자를 입력하실건가요? : ")) #입력받을 숫자의 개수를 입력받는다 
number = []             
for i in range(0, a):                            #반복문을 이용하여 a번만큼 숫자를 입력받고 number리스트에 추가한다
    b = int(input())                             #이후 오름차순을 해주는 sort함수를 이용하여 결과값을 출력한다
    number.append(b)
number.sort()
print(number)

