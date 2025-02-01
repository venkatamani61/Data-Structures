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
print("first element")
n1=Node(20)
n.next=n1
l.tail=n1
l.tail.next=l.head
l.head.next=l.tail
print("2 element: ")
l.insert_begin(30)
l.display()