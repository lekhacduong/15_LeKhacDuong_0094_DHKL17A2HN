class Date:
    def __init__(self, day = 8, month = 10, year = 2024):
        self.day =day
        self.month = month
        self.year = year
    
    def display(self):
        print("{}/{}/{}".format(self.day, self.month, self.year))
        
    def next(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            if self.day < 31:
                self.day += 1
            else:
                self.day = 1
                if self.month < 12:
                    self.month += 1
                else:
                    self.month = 1
                    self.year += 1
        elif self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                if self.day < 29:
                    self.day += 1
                else:
                    self.day = 1
                    self.month += 1
            else:
                if self.day < 28:
                    self.day += 1
                else:
                    self.day = 1
                    self.month += 1
        else:
            if self.day < 30:
                self.day += 1
            else:
                self.day = 1
                self.month += 1
    

def main():
    run = Date(29, 2, 2024)
    print("Ngay hom nay la: ")
    run.display()
    
    run.next()
    print("Ngay tiep theo la: ") 
    run.display()


if __name__ == "__main__":
    main()
    