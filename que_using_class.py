class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self):
        data=int(input("Enter the data :"))
        new_node=Node(data)
        if self.front==None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        
    def dequeue(self):
        if self.front==None:
            print("Queue is empty")
        elif self.front.next is None:#self.front==self.rear
            print("Popped element is:",self.front.data)
            self.front=None
        else:
            temp=self.front
            self.front=temp.next
            temp=None
    def display(self):
        if self.front is None:
            print("Queue is empty")    
        else:
            print("Elements of queue are:")
            temp=self.front
            while temp:
                print(temp.data)
                temp=temp.next
            print("\nFront:",self.front.data)
            print("\nRear:",self.rear.data)
q=Queue()
while(1):
    print("Enter the option from below:\n1-Enqueue operation\n2-Dequeue operation\n3-display")
    option=int(input())
    if option ==1:
        print("Enqueue operation ")
        q.enqueue()
    elif option ==2:
        print("Dequeue operation")
        q.dequeue()
    elif option ==3:
        print("Display")
        q.display()
    else:
        print("Enter correct option")
