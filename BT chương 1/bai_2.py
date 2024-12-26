class TS:
    def __init__(self, ho_ten = "", toan = 0, ly = 0, hoa = 0):
        self.ho_ten = ho_ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        
    def nhap_thong_tin(self):
        self.ho_ten = input("Nhap ho ten thi sinh: ")
        self.toan = int(input("Nhap diem toan: "))
        self.ly = int(input("Nhap diem ly: "))
        self.hoa = int(input("Nhap diem hoa: "))
        
    def tinh_tong_diem(self):
        return self.toan + self.ly + self.hoa
    
    def in_thong_tin(self):
        print("\nHo ten thi sinh: {}".format(self.ho_ten))
        print("Diem mon toan: {}".format(self.toan))
        print("Diem mon ly: {}".format(self.ly))
        print("Diem mon hoa: {}".format(self.hoa))
        print("Tong diem: {}".format(self.tinh_tong_diem()))
   
    
def main():
    danh_sach_ts = []
    so_luong_ts = int(input("Nhap so luong thi sinh: "))
    
    for _ in range(so_luong_ts):
        ts = TS()
        ts.nhap_thong_tin()
        danh_sach_ts.append(ts)
    
    print("\nDanh sach trung tuyen: ")
    danh_sach_ts.sort(key = lambda ts: ts.tinh_tong_diem(), reverse= True)
    for ts in danh_sach_ts:
        if ts.tinh_tong_diem() >= 20:
            ts.in_thong_tin()
            

if __name__ == "__main__":
    main()