#queue: abstract data tyoe with the
#Dequeue():
#Enqueue
#boolean Empty() : are there any elements?
#queue implementaion with linkded list
#with impleuemtation linked list
#enque : use list.pushback
#deque:use list.tipfront and lis.popfront
#empty:use list.empty

#rear is entry and front is exit or delete
#implementation with array
#enqueue :
#all operation are O(1) enqu
#linear queue is solved 
#using circular queue ,empty condition ,complete condiion, stack empty ,queue condition
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        newnode=Node(data)
        if self.front==None:
           self.front=newnode
           self.rear=newnode
        else:
            self.rear.left=newnode
            newnode.right=self.rear
            self.rear=newnode

    def front_ele(self):
        return "["+str(self.front.data)+"]"
    def rear_ele(self):
        return "["+str(self.rear.data)+"]"

    def dequeue(self):
        if self.front==None:
            print("Underflow")
        else:
            t=self.front
            self.front=self.front.left
            self.front.right=None
            return t.data

    def display(self):
        t=self.front
        while t.left:
            print("\033[1;35m["+str(t.data)+"]",end="<->")
            t=t.left
        print("["+str(t.data)+"]\033[0m")

#driver code

while True:
           ch=int(input("\033[1;32m__________________\n|choose Menu:    |\n|0.exit          |\n|1.create queue  |\n|2.enqueue       |\n|3.dequeue       |\n|4.display       |\n|5.rear          |\n|6.front         |\n|________________|\033[0m"))
           print("\033[1;34m")
           if ch==0:
                break
           elif ch==1:
                q=queue()
           elif ch==2:
                q.enqueue(int(input("enter the element: ")))
                print("element added successfully")
           elif ch==3:
                print("dequeue opperation : "+str(q.dequeue()))
           elif ch==4:
                q.display()
           elif ch==6:
                print("front element: "+q.front_ele())
           elif ch==5:
                print("rear element: "+q.rear_ele())
           else:
               print("plz enter correct option!")
print("\033[0m")
































