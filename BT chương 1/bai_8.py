class Date:
    def __init__(self, day = 0, month = 0, year = 0):
        self.day =day
        self.month = month
        self.year = year
    
    def hien_thi(self):
        print("{}/{}/{}".format(self.day, self.month, self.year))
        
    


class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao = ngay_vao
        
    def display(self):
        print("Ho va ten nhan vien la: {}".format(self.ho_ten))
        print()
        print()


        
def main():
    
    
    print("Nhap thong tin nhan vien")
    ten = input("Nhap ten nhan vien: ")
    ngay_sinh = int(input("Nhap ngay sinh: "))
    thang_sinh = int(input("Nhap thang sinh: "))
    nam_sinh = int(input("Nhap nam sinh: "))
    ngay_vao = int(input("Nhap ngay vao: "))
    thang_vao = int(input("Nhap thang vao: "))
    nam_vao = int(input("Nhap nam vao: "))
    
    ngay_sinh_nhat = Date(ngay_sinh, thang_sinh, nam_sinh)
    ngay_vao_cong_ty = Date(ngay_vao, thang_vao, nam_vao)
    
    nhan_vien = Employee(ten, ngay_sinh_nhat, ngay_vao_cong_ty)
    print("\nThong tin nhan vien la ")
    print("Ho ten nhan vien la: ")
    nhan_vien.display()
    print("Ngay sinh nhan vien la: ")
    nhan_vien.display


if __name__ == "__main__":
    main()