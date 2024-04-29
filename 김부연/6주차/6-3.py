N = int(input("숫자 몇개를 입력받은 것인지 알려주세요:"))
number_list =[]

for i in  range(N):
    a= int(input("숫자를 입력해주세요:"))
    number_list.append(a)

final_numbers = list(set(number_list))
final_numbers.sort()

for i in final_numbers:
    print(i)
    
 
