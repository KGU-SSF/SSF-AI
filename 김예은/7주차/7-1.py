class Rectangle:
    # 클래스 변수
    width = height = 0

    #[생성자]
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        return area

    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum

# class object 생성
print('-' * 30)
rec = Rectangle(10, 5)  # x 초기화
area = rec.area_calc()  # 분산 함수 호출
print('사각형의 넓이:', area)

circum = rec.circum_calc()  
print('사각형의 둘레:', circum)
print('-' * 30)