# queue=[]
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.append(5)
# p=queue.pop(0)
# print(p)
# f=queue[0]
# print(f)
# is_empty=len(queue)==0
# size=len(queue)
# print(is_empty)
# print(size)

queue=list()
def enqueue():
    n=int(input("Enter data:"))
    queue.append(n)
    print("Queue with inserted data:")
    print("--------")
def dequeue():
    if len(queue)==0:
        print("Queue is empty")
        print("--------")
    else:
        queue.pop(0)#del queue[0]
        print("deleting front")
        print("--------")
def display():
      if len(queue)==0:
        print("Queue is empty")
        print("--------")
      else:
        print("elements in queue are")
        for i in queue:
            print(i)
        print("Front:",queue[0])
        print("REAR:",queue[-1])

while(1):
    print("Enter the option from below:\n1-Enqueue operation\n2-Dequeue operation\n3-display")
    option=int(input())
    if option ==1:
        print("Enqueue operation ")
        enqueue()
    elif option ==2:
        print("Dequeue operation")
        dequeue()
    elif option ==3:
        print("Display")
        display()
    else:
        print("Enter correct option")
