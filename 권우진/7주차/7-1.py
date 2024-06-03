

class Rectangle:

    width = height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        return self.width * self.height

    def circum_calc(self):
        return (self.width + self.height) * 2

if __name__ == "__main__":
    print('-' * 30)

    rec = Rectangle(10, 5)
    print('사각형의 넓이: ', rec.area_calc())
    print("사각형의 둘레: ", rec.circum_calc())

    print('-' * 30)
