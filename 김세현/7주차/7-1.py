w=int(input("가로 길이:"))
h=int(input("세로 길이:"))

class Rectangle:
 width = height = 0
 
class Rectangle:
        def __init__(self, width, height):
                self.width = width
                self.height = height
        def area_calc(self):
                area = self.width * self.height
                return area

        def circum_calc(self):
                circum = (self.width + self.height) * 2
                return circum
        
# class object 생성
print('-'*30)
rec = Rectangle(w, h) # x 초기화
area = rec.area_cals() # 분산 함수 호출
print('사각형의 넓이:', area)

circum = rec.circum_calsc()
print('사각형의 둘레:', circum)
print('-'*30)