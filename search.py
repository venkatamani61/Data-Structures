#insertion at position using position value
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
                
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            count=0
            while temp:
                print(temp.data,"-->",end="")
                count+=1
                temp=temp.next
            print("\ncount of elements:",count)
            

l=SLL()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
l.insert_pos(1,500)
l.display()
        
        
