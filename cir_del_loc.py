class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_begin(self,data):
        new_node=Node(data)
        if self.head.data is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head

    def insert_location(self,data,position):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=self.head 
            return
        if position==0:
            new_node.next=self.head
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=new_node
            self.head=new_node
        current=self.head  
        count=0
        while count<position-1 and current.next!=self.head:
            current=current.next
            count+=1      
        new_node.next=current.next
        current.next=new_node

    def delete_location(self,position):
        
        
    def display(self):
        if self.head is None:
            print("--empty--")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
l=CLL()
n=Node(10)
l.head=n

n1=Node(20)
n.next=n1
l.tail=n1
l.tail.next=l.head
l.head.next=l.tail

l.insert_begin(30)
l.insert_location(23,1)
l.display()