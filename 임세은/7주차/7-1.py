class Rectangle:
# 클래스 변수
 width = height = 0
 
 # 생성자를 이용하여 높이와 넓이를 정의함
 def __init__(self,width,height):
     self.width=width
     self.height=height
 
 def area_calc(self):
    area = self.width * self.height
    return area
 
 def circum_calc(self):
    circum = (self.width + self.height) * 2
    return circum


# class object 생성
print('-'*30)
rec = Rectangle(10, 5) # 초기화
area = rec.area_calc() # 넓이 계산 메소드
print('사각형의 넓이:', area)

circum = rec.circum_calc()  # 둘레 계산 메소드
print('사각형의 둘레:', circum)
print('-'*30)