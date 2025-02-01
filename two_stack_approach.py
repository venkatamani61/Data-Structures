#parallel approach
class TwoStackEqualSpace:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.mid=(n+1)//2
        self.top1=-1
        self.top2=self.mid-1
    
    #push operation for stack1 
    def push1(self,data):
        if self.top1<self.mid-1:
            self.top1=self.top1+1
            self.arr[self.top1]=data
            print(f"PUSHed {data} into stack1")
        else:
            print("stack1 is overflow")

    #push operation for stack2
    def push2(self,data):
        if self.top2<self.size-1:
            self.top2=self.top2+1
            self.arr[self.top2]=data
            print(f"pushed {data} into stack2")
        else:
            print("stack2 is overflow or full")
    
    #pop operation for stack1
    def pop1(self):
        if self.top1>=0:
             data=self.arr[self.top1]
             self.arr[self.top1]=None
             self.top1-=1
             print(f"poped {data} from stack1.")
             return data
        else:
            print("stack is underflow")
            return None
    
    #pop operation for stack2
    def pop2(self):
        if self.top2>=self.mid:#if self.top2<self.size:
            data=self.arr[self.top2]
            self.top2-=1
            print(f"poped {data} from stack2")
            return data
        else:
            print("stack is underflow")
            return None

    #display operation
    def display(self):
        print(f"Array:{self.arr}")
        print(f"stack1:{self.arr[:self.mid]}")
        print(f"stack2:{self.arr[self.mid:]}")

#a=int(input("enter size of stack: "))
tse=TwoStackEqualSpace(8)
tse.display()
tse.push1(9)
tse.push2(1)
tse.display()
tse.push1(10)
tse.push2(20)
tse.display()
tse.pop1()
tse.display()