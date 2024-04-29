class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area_calc(self):
        area = (self.height * self.width)
        return area
    def circum_calc(self):
        circum = (self.height + self.width)*2
        return circum
print('-'*30)
rec = Rectangle(10, 5)
area = rec.area_calc()
print('사각형 넓이:',area)

circum= rec.circum_calc()
print('사각형 둘레:',circum)
print('-'*30)