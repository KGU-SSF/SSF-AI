w = int(input("가로를 입력하세요: "))
l = int(input("세로를 입력하세요: "))

class calculate:
    wid = led = 0
    def __init__ (self, wid, led):
        self.wid = wid
        self.led = led
    def area_clac(self):
        area = (self.wid*self.led)
        return area
    def round_clac(self):
        round = (self.wid+self.led)*2
        return round
    
cal = calculate(w,l)
print('-'*30)
area = cal.area_clac()
print("사각형의 넓이=",area)
round = cal.round_clac()
print("사각형의 둘레=",round)
print('-'*30)