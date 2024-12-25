import json

class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = None
        
    def doc_json(self):
        with open(self.file_path, 'r', encoding = 'utf-8') as file:
            self.root = json.load(file)
            
    def hien_thi(self):
        if self.root:
            for user in self.root:
                print(f"Name: {user['name']}, Age: {user['age']}, Address: {user['address']}")
                

path = './LAB 1//data//users.json'
read = JSONReader(path)
read.doc_json()
read.hien_thi()