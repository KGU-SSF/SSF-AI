class Rectangle:
    # 클래스 변수
    width = height = 0
    
    def __init__(__self__, width, height):  # 생성자를 정의하는 부분
        __self__.width = width              # self를 사용해 밑변을 정의하는 부분
        __self__.height = height            # self를 사용해 높이를 정의하는 부분

    def area_calc(self):
        area = self.width * self.height
        return area
    
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum
    
# class object 생성

print('-'*30)
rec = Rectangle(10,5)   # x 초기화
area = rec.area_calc()  # 분산 함수 호출
print('사각형의 넓이:', area)

circum = rec.circum_calc()
print('사각형의 둘레:', circum)
print('-'*30)