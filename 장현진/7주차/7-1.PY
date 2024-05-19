class Rectangle:
    width=height=0
    def__init__(self,width,height):
        self.width=width
        self.height=height
    def area_calc(self):
        erea=self.width*self.height
        return area
    def circum_calc(self):
        circum=(self.width+self.height)*2
        return circum
print('-')*30
print('-'*30)
rec = Rectangle(10, 5) 
area = rec.area_calc() 
print('사각형의 넓이:', area)
print('-'*30)
circum=rec.circum_calc()
print('사각형의 둘레:',circum)
print('-'*30)