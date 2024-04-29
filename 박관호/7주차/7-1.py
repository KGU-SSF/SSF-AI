class Rectangle : 
    
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        
    def area_calc(self):
        area = self.width * self.height
        return area
    
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum
    
print('-'*30)
width = int(input("너비를 입력하시오 : "))
height = int(input("높이를 입력하시오 : "))
rec = Rectangle(width, height) 
area = rec.area_calc() 
print('사각형의 넓이:', area)
circum = rec.circum_calc()
print('사각형의 둘레:', circum)
print('-'*30)