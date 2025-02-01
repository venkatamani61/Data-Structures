class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularQueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def empty(self):
        return self.front is None
    def enqueue(self,data):
        new_node=Node(data)
        if self.empty():
            self.front=new_node
            self.rear=new_node
            self.rear.next=self.front
        else:
            self.rear.next=new_node
            self.rear=new_node
            self.rear.next=self.front
    def dequeue(self):
        if self.empty():
            print("Queue has no elements")
        item=self.front.data
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.rear.next=self.front
            
            print("deleted node element: ",self.front.data)

    def peek(self):
        print("peek:",self.front.data)
    
    def display(self):
        if self.empty():
            print("queue have no elements")
        else:
            temp=self.front
            print(temp.data,end="-->")
            while temp.next!=self.front:
                temp=temp.next
                print(temp.data,end="-->")
            print()
cq=CircularQueue()
cq.enqueue(12)
cq.enqueue(13)
cq.display()