import math
class hinh_da_giac:
    def __init__(self, canh):
        self.canh = canh
        
    
    def chu_vi(self):
        pass
    
    def dien_tich(self):
        pass
    
class hinh_binh_hanh(hinh_da_giac):
    def __init__(self, chieu_dai, chieu_rong, duong_cao = 0):
        super().__init__(4)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        self.duong_cao = duong_cao
    
    def chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    
    def dien_tich(self):
        self.duong_cao = math.sqrt((self.chieu_dai ** 2) + (self.chieu_rong ** 2))
        return self.chieu_dai * self. duong_cao
    
class hinh_chu_nhat(hinh_binh_hanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)
    
    def chu_vi(self):
        return super().chu_vi()
    
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong        
    
class hinh_vuong(hinh_chu_nhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        
    def chu_vi(self):
        return super().chu_vi()
    
    def dien_tich(self):
        return super().dien_tich()
    
def main():
    hbh = hinh_binh_hanh(3, 4)
    print("Chu vi hbh la: ", hbh.chu_vi())
    print("Dien tich hbh la: ", hbh.dien_tich())
    hcn = hinh_chu_nhat(5, 6)
    print("Chu vi hcn la: ", hcn.chu_vi())
    print("Dien tich hcn la: ", hcn.dien_tich())
    hv = hinh_vuong(7) 
    print("Chu vi hv la: ", hv.chu_vi())
    print("Dien tich hv la: ", hv.dien_tich())

if __name__ == "__main__":
    main()