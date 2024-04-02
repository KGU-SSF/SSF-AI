a = int(input())
if a < 101 and a > 0:
    for i in range(1, a + 1) :              
        print(" " * (a-i), end="")
        for j in range(i):
            print("* ", end = "")            
        print() 
else:
    exit()
    
#중앙 정렬을 위해 center 함수를 사용해봤는데 모양이 깨져 실패.

# a = int(input())
# for i in range(1, a + 1):  
#     b = "*" * (i-1) 
#     print(b.center(a, ' ')) 