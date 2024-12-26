class hinhchunhat:
    def __init__(self, chieu_dai = 0, chieu_rong = 0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def nhap_du_lieu(self):
        self.chieu_dai = int(input("Nhap chieu dai hcn: "))
        self.chieu_rong = int(input("Nhap chieu rong hcn: "))
    
    def tinh_chu_vi(self):
        self.chu_vi = (self.chieu_dai + self.chieu_rong) * 2
        return self.chu_vi
    
    def tinh_dien_tich(self):
        self.dien_tich = self.chieu_dai * self.chieu_rong
        return self.dien_tich

    def hien_thi_du_lieu(self):
        print("Chieu dai hcn: ", self.chieu_dai)
        print("Chieu rong hcn: ", self.chieu_rong)
        print("Chu vi hcn: ", self.tinh_chu_vi())
        print("Dien tich hcn: ", self.tinh_dien_tich())


hinh_chu_nhat = hinhchunhat()
hinh_chu_nhat.nhap_du_lieu()
hinh_chu_nhat.hien_thi_du_lieu()