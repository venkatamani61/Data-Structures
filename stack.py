# stack=[]
# stack.append(10)#push operation
# stack.append(11)
# stack.append(12)
# stack.append(13)
# print(stack)
# top_element=stack[-1]#top or peak operation
# print(top_element)
# print(stack.pop())#pop operation
# print(stack)
# print(stack[-1])
# size=len(stack)
# print(size)
# is_empty=len(stack)==0
# print(is_empty)




#stack using function
'''def push():
    n=int(input("enter element: "))
    stack.append(n)
    print(stack)
def pop():
    print(stack.pop())
def top():
    print(stack[-1])
def size():
    print(len(stack))
def isempty():

    print(len(stack)==0)
stack=[6,7,2,3]
print("0:push operation")
print("1:pop operation")
print("2:top or peak operation ")
print("3:size operation")
print("4:is empty operation")
choice=input("enter option:")

while choice:
    if choice=="0":
         push()
         
    elif choice=="1":
         pop()
    elif choice=="2":
         top()
    elif choice=="3":
         size()
    elif choice=="4":
        isempty()
    else:
        print("invalid option")
    break
'''

'''stack=[1,2,3,4]
stack=list[::-1]
print(stack)
stack.insert(0,7)
print(stack)
'''

'''

def push():
    n=int(input("enter element: "))
    if len(stack)==0:
      stack.append(n)
    else:
        stack.insert(0,n)
    print(n," is inserted into stack")
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack[0],"element is deleted")
        del stack[0]
        print(stack,"after deletion")
    
def top():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack[0],"is top element of the stack")
def size():
    size=len(stack)
    print("the  length of the stack is",size)
    
def isempty():
    print(len(stack)==0)

def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("elements of stack are:")
        for i in stack:
            print(i)
stack=list()


while True:
    print("0:push operation")
    print("1:pop operation")
    print("2:top or peak operation ")
    print("3:size operation")
    print("4:is empty operation")
    choice=input("enter option:")
    if choice=="0":
        print("PUSH OPERATION")
        push()
         
    elif choice=="1":
        print("POP OPERATION")
        pop()
    elif choice=="2":
         top()
    elif choice=="3":
         size()
    elif choice=="4":
        isempty()
    else:
        print("invalid option")
'''
    

'''
class stack:
    def __init__(self):
        self.items=list()
    def push(self,item):
        self.items.append(item)
        return self.items
    def pop(self):
        return self.items.pop()
    def peek(self):
        if len(self.items)==0:
            return "----empty---"
        else:
            return self.items[-1]
    def isEmpty(self):
         return len(self.items)==0
    def size(self):
        return len(self.items)
obj=stack()
print(obj.push(10))
print(obj.push(20))
print(obj.push(30))
print(obj.push(40))
print(obj.pop())
print(obj.peek())
print(obj.isEmpty())
print(obj.size())


'''




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self):
        data=int(input("enter element to insert into stack"))
        new_node=Node(data)
        if self.top is None:
            self.top=new_node
            self.top.next=None
        else:
            new_node.next=self.top
            self.top=new_node
    def pop(self):
        if self.top is None:
            print("stack is empty")
        elif self.top.next is None:
            print("popped data is:",self.top.data)
            self.top=None
        else:
            temp=self.top
            print("popped data is :",self.top.data)
            self.top=temp.next
            temp=None
    #def peek():
    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            print("Elements of the stack are:")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top of the stack :",self.top.data)

s=stack()
while (1):
    print("1:push")
    print("2:pop")
    print("3:display")
    a=input("enter option:")
    if a=="1":
        print("push operation")
        s.push()
    elif a=="2":
        print("pop operation")
        s.pop()
    elif a=="3":
        print("display opreration")
        s.display()
    else:
        print("invalid option")
            



# class __init__(self,max_size):
#     self.stack=[0]*max_size
#     self.top=-1
#     self.max_size=max_size





                




















