"""
아래와 같이 리스트의 데이터를 출력하라.
단, for문과 range문을 사용하시오.
입력예시 : price_list = [32100, 32150, 32000, 32500]
출력예시 : 
32100
32150
32000
32500
"""


list_1 = input('리스트 입력 : ')
list_2 = list_1.replace('=', '')
list_3 = list_2.replace('[', '')
list_4 = list_3.replace(']', '')
list_5 = list_4.replace(' ', '', 1)
list_6 = list_5.replace(',', '')

list = list_6.split()

for i in list[1:] :
    print(i)