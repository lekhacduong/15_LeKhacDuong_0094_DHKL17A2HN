import math

class Diem:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
class Elip(Diem):
    def __init__(self, x = 0, y = 0, a = 0, b= 0):
        super().__init__(x, y)
        self.a = a
        self.b = b
    
    def dien_tich(self):
        return math.pi * self.a * self.b
    
class hinh_tron(Elip):
    def  __init__(self, a = 0 , b = 0, r = 0):
        super().__init__(x = 0, y = 0, a = r, b = r)
        
    def dien_tich(self):
        return super().dien_tich()

def main():
    x = float(input("Nhập vào hoành độ x: "))
    y = float(input("Nhập vào tung độ y: "))
    a = float(input("Nhập vào bán trục lớn a: "))
    b = float(input("Nhập vào bán trục nhỏ b: "))
    r = float(input("Nhập vào bán kính r: "))
    elip = Elip(x, y, a, b)
    htron = hinh_tron(a, b, r)
    
    print("Dien tich hinh elip la: ", elip.dien_tich())
    print("Dien tich hinh tron la: ", htron.dien_tich())

if __name__ == "__main__":
    main()