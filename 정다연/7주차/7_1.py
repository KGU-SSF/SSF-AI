class Rectangle:

    width = height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area_calc(self):
        area = self.width * self.height
        return area
    
    def circum_calc(self):
        circum = (self.width + self.height)*2
        return circum

# [생성자]
# 생성자를 정의하는 부분
# self를 사용해 넓이를 정의하는 부분
# self를 사용해 높이를 정의하는 부분
 
    def area_calc(self):
        area = self.width * self.height
        return area
    
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum
    
# class object 생성
print('-'*30)
pok = int(input('폭:'))
nopi = int(input('높이:'))

rec = Rectangle(pok, nopi) # x 초기화
area = rec.area_calc() # 분산 함수 호출
print('사각형의 넓이:', area)

circum = rec.circum_calc()
print('사각형의 둘레:', circum)
print('-'*30)