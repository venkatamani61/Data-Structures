
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
     
    def insert_pos(self,pos_value,data):
        node_pos=Node(data)
        
        temp=self.head
        for i in range(pos_value-1):
            temp=temp.next
        node_pos.data=data
        node_pos.next=temp.next
        temp.next=node_pos

    def del_end(self):
        previous=self.head
        temp=self.head.next
        
        while temp.next is not None:
            temp=temp.next
            previous=previous.next
        previous.next=None  
    def del_pos(self,pos_val):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos_val-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next 

            

                
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
            print()

l=SLL()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3

l.del_pos(3)      
l.display()       
