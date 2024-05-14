class Rectangle:
# 클래스 변수
    width = height = 0

    def __init__(self,width,height):
        self.width = width
        self.height = height

 # 넓이 계산
    def area_calc(self):
        area = self.width * self.height
        return area

 # 둘레 계산
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum
# class object 생성
print('-'*30)

w = int(input("가로 길이를 입력하세요: "))
h = int(input("세로 길이를 입력하세요: "))

rec = Rectangle(w, h)
area = rec.area_calc() # 분산 함수 호출
print('사각형의 넓이:', area)
circum = rec.circum_calc()
print('사각형의 둘레:', circum)
print('-'*30)