준서 = int(input())
if 준서 <= 50:
    준서 = 50
이다 = int(input())
if 이다 <= 50:
    이다 = 50
홍다 = int(input())
if 홍다 <= 50:
    홍다 = 50
우진 = int(input())
if 우진 <= 50:
    우진 = 50
우현 = int(input())
if 우현 <= 50:
    우현 = 50

X = [준서, 이다, 홍다, 우진, 우현]
result = sum(X)
print(f"평균 성능 : {result / len(X)}")