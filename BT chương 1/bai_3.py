class PS:
    def __init__(self, tu_so = 0, phan_so = 0):
        self.tu_so = tu_so
        self.phan_so = phan_so
        
    def kiem_tra_phan_so(self):
        if self.mau_so == 0:
            return False
        return True
    
    def nhap_phan_so(self):
        self.tu_so = int(input("Nhap tu so: "))
        self.mau_so = int(input("Nhap mau so: "))
        
    
    def in_phan_so(self):
        if self.kiem_tra_phan_so():
            print("Phan so nhap vao la: {} / {}".format(self.tu_so, self.mau_so))
        else:
            print("Phan so nhap vao khong hop le")

phan_so = PS()
phan_so.nhap_phan_so()
phan_so.in_phan_so()