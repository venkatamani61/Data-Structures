#inserting data after 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
     
    def afterdata(self,dataafter,item):
        new_node=Node(item)
        temp=self.head
        while temp.next is not None and temp.data is not dataafter:
            temp=temp.next
        if temp.next is not None:
            new_node.next=temp.next
            temp.next=new_node
        elif temp.data is not dataafter:
            print("node is not present")
        else:
            new_node.next=None
            temp.next=new_node


                
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next     
l=SLL()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
l.afterdata(20,67)
l.display()
        
        
