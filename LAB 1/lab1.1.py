import xml.etree.ElementTree as ET 

class XMLReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = None
        
    def doc_xml(self):
        tree = ET.parse(self.file_path)
        self.root = tree.getroot()
    
    def hien_thi(self):
        if self.root:
            for product in self.root.findall('product'):  # tra ve danh sach cac phan tu trong tap tin xml
                name = product.find('name').text          # tra ve phan tu dau tien duoc tim thay trong cay
                price = product.find('price').text
                quantity = product.find('quantity').text
                print(f'Product: {name}, Price: {price}, Quantity: {quantity}')



path = 'LAB 1\data\products.xml'
read = XMLReader(path)
read.doc_xml()
read.hien_thi()
