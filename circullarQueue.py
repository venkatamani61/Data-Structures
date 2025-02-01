class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=-1
        self.rear=-1

    def isFull(self):
        return self.front==(self.rear+1)%self.size# if (self.rear+1)%self.size==0:
        #or
        #return (self.rear+1==self.size and self.front==0)or(self.rear+1==self.front)

    def isEmpty(self):
        return self.front==-1

    def enqueue(self,data):
        if self.isFull():
            print("circular queue is overflow")
        if self.isEmpty():
            self.front=0
        if self.rear+1==self.size:
            self.rear=0
        else:
            self.rear=self.rear+1

        #or
        #self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=data
        print(f"enqueue:{data}")
     

    def dequeue(self):
        if self.isEmpty():
           print("Queue is empty")
        item=self.queue[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        if self.front+1==self.size:
            self.front=0
        else:
            self.front=self.front+1
        print("Dequeue:",item)
        return item
    def peek(self):
        return self.queue[self.front]
    
    def display(self):
        if self.isEmpty():
           print("Queue is empty")
           return
        if self.rear>=self.front:
            print("queue elements:",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
        else:
            print("Queue elements:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")

cq=CircularQueue(8)
cq.enqueue(10)
cq.enqueue(110)
cq.enqueue(120)
cq.enqueue(130)
cq.enqueue(140)
cq.enqueue(150)
cq.display()
cq.enqueue(120)
cq.dequeue()
print(cq.peek())
cq.display()








