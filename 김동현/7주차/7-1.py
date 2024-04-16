class Rectangle:
    width = height = 0
    
    def __init__(self, width, height): # 생성자 정의
        self.width = width # self사용해 넓이 정의
        self.height = height # self사용해 높이 정의

    def area_calc(self):
        area = self.width * self.height
        return area

    def circum_clac(self):
        circum = (self.width + self.height)*2
        return circum

print('-'*30)
rec = Rectangle(10, 5)
area = rec.area_calc()
print('사각형의 넓이: ', area)

circum = rec.circum_clac()
print('사각형의 둘레: ', circum)
print('-'*30)