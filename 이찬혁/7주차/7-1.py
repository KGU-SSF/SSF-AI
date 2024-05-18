class Rectangle:
    width = height = 0
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area_calc(self):
        area = self.width * self.height
        return area
    def circum_calc(self):
        circum = (self.width+self.height)*2
        return circum

print('"너비 높이"의 형태로 입력해주세요(" 제외)')
wh = input()
wh = wh.split(' ')
w = int(wh[0])
h = int(wh[1])
print('-'*30)
rec = Rectangle(w, h)
area = rec.area_calc()
print('사각형의 넓이:',area)
circum = rec.circum_calc()
print('사각형의 둘레',circum)
print('-'*30)
        