class Stack:
    def __init__(self, limit_stack):
        self.limit_stack = limit_stack
        self.float_stack = []
   
   
    # ham dua mot phan tu vao trong stack
    def push(self, element):
        return self.float_stack.append(element)
        
        
    # ham lay mot phan tu ra khoi dinh stack
    def pop(self):
        return self.float_stack.pop()
    
    
    # kiem tra stack trong
    def isEmpty(self):
        if len(self.float_stack) == 0:
            return "Stack trong"
        else:
            return "Stack co ky tu"
    
    
    # ham kiem tra xem ngan xep da day chua
    def isFull(self):
        if len(self.float_stack) == self.limit_stack:
            return "Stack da day"
        else:
            return "Stack chua day"
      
    # ham huy stack
    def __del__(self):
        print("Huy stack")
        del self.float_stack
        
    # them ham count bai 5    
    def count(self):
        return len(self.float_stack)
    
    # them ham print bai 6
    def print(self):
        return self.float_stack


# vidu
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.push(5)
stack.push(6)

print("Ngan xep trong: ", stack.isEmpty())
print("Ngan xep day: ", stack.isFull())
print("So phan tu trong stack: ", stack.count())
print("Noi dung stack la: ", stack.print())

del stack