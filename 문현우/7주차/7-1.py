class Rectangle: #class는 대문자로 시작하는것이 좋음
    width=height=0
    def __init__(self,width,height):#__init__사용하여 생성자 생성
        self.width=width
        self.height=height
    
    def area_calc(self):
        area=self.width * self.height
        return area
    
    def circum_calc(self):
        circum=(self.width + self.height) *2
        return circum

print('-'*30)
rec=Rectangle(10,5) #클래스 객체 생성
area=rec.area_calc()
print('사각형의 넓이:',area)

circum=rec.circum_calc()
print('사각형의 둘레:',circum)
print('-'*30)