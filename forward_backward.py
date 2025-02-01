class forback:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*size
        self.top1=-1
        self.top2=size
    
    #push1
    def push1(self,data):
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1]=data
            print(f"pushed {data} into stack")
        else:
            print("stack is overflow")
    
    #push2
    def push2(self,data):
        if self.top2>self.top1:
            self.top2-=1
            self.arr[self.top2]=data
            print(f"pushed {data} into stack")
        else:
            print("stack is overflow")
        
    #pop1
    def pop1(self):
        if self.top1>=0:
            data=self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            print(f"poped {data} from stack")
     #pop2       
    def pop2(self):
        if self.top1<self.size:
            data=self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2+=1
            print(f"poped {data} from stack")
    def display(self):
        print("array is:",self.arr)
        print("stack1:",self.arr[self.top1:self.top2])
        print("stack2:",self.arr[self.top2:])
fb=forback(5)
fb.push1(10)
fb.push2(20)
fb.display()
fb.push2(20)
fb.push1(10)
fb.display()
fb.pop1()
fb.pop2()
fb.display()
