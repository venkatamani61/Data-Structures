'''#basic 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        #self.next=False
        #self.next=0
        #self.next=[]
class SLL:
    def __init__(self):
        self.head=None
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
l.display()'''




'''
#isert at begining
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        #self.next=False
        #self.next=0
        #self.next=[]
class SLL:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node


        
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
l.insert_begin(5)
l.display()
'''


#insert at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        #self.next=False
        #self.next=0
        #self.next=[]
class SLL:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node   


        
    def display(self):
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
l=SLL()

l.insert_end(5)
l.display()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
l.insert_end(90)
l.display()














