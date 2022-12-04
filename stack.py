class Stack:
    def __init__(self,cap=5):
        self.cap=cap
        self.A=[]
        self.top=-1
    def push(self,data):
        if self.is_full():
            print("Overflow")
            return
        self.A.append(data)
        self.top+=1
        print(f"pushed {data}")
        
    def pop(self):
        if self.is_empty():
            print("Underflow")
            return
        self.top-=1
        return self.A[self.top]
    def peek(self):
        return self.A[self.top]
    def size(self):
        return self.top+1
    def is_empty(self):
        if self.top ==-1:
            return True
        return False
    def is_full(self):
        return self.top+1==self.cap

S=Stack()


for i in range(10):
    S.push(i)
