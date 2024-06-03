class Rectangle:
    width = height = 0
    
    def __init__(self,width,height):

        self.height = height
        self.width = width

    def area_calc(self):
        area =self.width * self.height
        return area
    
    def cirecum_calc(self):
        circum = (self.width + self.height) * 2
        return circum
    
print("-"*30)
rec = Rectangle(10, 5)
area = rec.area_calc()
print('사각형의 넓이 : ', area)

circum = rec.cirecum_calc()
print('사각형의 둘레 : ',circum)
print('-'*30)