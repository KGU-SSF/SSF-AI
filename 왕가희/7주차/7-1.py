class Rectangle:
    width = height = 0

def __init__(self , width, height):
    self .width = width
    self .height = height

def area_calc(self):2
    area = self.width * self.height
    return area

def circum_calc(self):
    circum = (self.width + self.height) * 2
    return circum

print('-'*30)
rec = Rectangle(w, h) 
area = rec.area_cals()
printf('사각형의 넓이: ', area)

circum = rec.circum_calc()
printf('사각형의 둘레 : ', circum)
printf('_'*30)