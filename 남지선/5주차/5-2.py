# 예제를 보고 규칙을 유추한 뒤에 피라미드를 만들어 봅시다.
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

num=int(input("숫자를 입력하세요: "))

sta=1
null=int(num-2)

for i in range(num):
    
    if i==(num-1): 
        print("* "*sta)
        continue
    
    print((" "*null)+" *"*sta)
    
    sta+=1
    null-=1