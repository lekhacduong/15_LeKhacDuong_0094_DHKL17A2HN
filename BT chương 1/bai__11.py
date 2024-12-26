import math

class tam_giac:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        s = self.chu_vi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class tam_giac_vuong(tam_giac):
    def __init__(self, a=0, b=0, c=0):
        super().__init__(a, b, c)
        if a**2 + b**2 != c**2:
            raise ValueError("Không phải là tam giác vuông")

    def dien_tich(self):
        return 0.5 * self.a * self.b


class tam_giac_can(tam_giac_vuong):
    def __init__(self, a=0, b=0, c=0):
        super().__init__(a, b, c)
        if a != b and a != c and b != c:
            raise ValueError("Không phải là tam giác cân")

    def dien_tich(self):
        s = self.chu_vi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class tam_giac_deu(tam_giac_can):
    def __init__(self, a=0, b=0, c=0):
        super().__init__(a, b, c)
        if a != b or a != c:
            raise ValueError("Không phải là tam giác đều")

    def dien_tich(self):
        return (math.sqrt(3) / 4) * self.a ** 2
    
def main():
    a = int(input("Nhập vào cạnh a: "))
    b = int(input("Nhập vào cạnh b: "))
    c = int(input("Nhập vào cạnh c: "))
    tamgiac = tam_giac(a, b, c)
    tamgiacvuong = tam_giac_vuong(a, b, c)
    tamgiacdeu = tam_giac_deu(a, b, c)
    tamgiaccan = tam_giac_can(a, b, c)
    print("Chu vi tam giac la: ", tamgiac.chu_vi())
    print("Dien tich tam giac la: ", tamgiac.dien_tich())
    print("Dien tich tam giac vuong la: ", tamgiacvuong.dien_tich())
    print("Dien tich tam giac deu la: ", tamgiacdeu.dien_tich())
    print("Dien tich tam giac canla: ", tamgiaccan.dien_tich())

if __name__ == "__main__":
    main()