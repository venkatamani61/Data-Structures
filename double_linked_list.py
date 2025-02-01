class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None

    #insertion at begining
    def insert_begin(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head

        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp


        
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
            print()
    def search(self,value):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            count=0
            while temp.data is not value:
                #if temp.data==value:
                count+=1
                temp=temp.next             
            print(count+1)
l=DLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
n5=Node(50)
n4.next=n5
n5.prev=n4
l.insert_begin(10)
l.insert_end(20)
l.display()
l.search(40)