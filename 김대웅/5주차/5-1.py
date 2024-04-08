A = int(input("첫 번째 성능을 입력하시오 :"))
B = int(input("두 번째 성능을 입력하시오 :"))
C = int(input("세 번째 성능을 입력하시오 :"))
D = int(input("네 번째 성능을 입력하시오 :"))
E = int(input("다섯 번째 성능을 입력하시오 :"))
if 0 < A < 50:
    A = 50
if 0 < B < 50:
    B = 50
if 0 < C < 50:
    C = 50
if 0 < D < 50:
    D = 50
if 0 < E < 50:
    E = 50
print(int((A+B+C+D+E)/5))