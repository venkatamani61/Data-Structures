max_size=5
queue=[]
def enqueue(max_size,queue,data):
    if len(queue)>=max_size:
        print("Queue is over flow")
    else:
        queue.append(data)
        print("Added element is:",data)
def dequeue(queue):
    if len(queue)==0:
        print("Queue is empty")
    else:
        data=queue.pop(0)
        print("popped element from the queue is ",data)
    print("-------")
def display(queue):
    if len(queue)==0:
        print("Queue is empty")
    else:
        print("elements of Queue are",queue)
    
        print("front:",queue[0])
        print("rear:",queue[-1])
while(1):
    print("Enter the option from below:\n1-Enqueue operation\n2-Dequeue operation\n3-display")
    option=int(input())
    if option ==1:
        print("Enqueue operation ")
        n=int(input("enter data:"))
        enqueue(max_size,queue,n)
    elif option ==2:
        print("Dequeue operation")
        dequeue(queue)
    elif option ==3:
        print("Display")
        display(queue)
    else:
        print("Enter correct option")
