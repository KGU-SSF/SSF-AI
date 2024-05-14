class Renctangle:
    width = height = 0
    
    def __init__(self, width, height): #객체를 초기화함
        self.width = width #입력된 width값을 오른쪽 width에 할당함
        self.height = height #입력된 height값을 오른쪽 height에 할당함
    
    def area_calc(self):
        area = self.width * self.height
        return area
    
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum

print('-'*30)
rec = Renctangle(10 , 5)
area = rec.area_calc()
print('사각형의 넓이: ',area)

circum = rec.circum_calc()
print('사각형의 둘레: ', circum)
print('-'*30)