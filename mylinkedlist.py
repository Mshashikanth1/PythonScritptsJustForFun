class Node:
    def __init__(self,data):
        self.data=data
        self.next=data
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def pushback(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=self.tail.next
            
    def pushfront(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def popback(self):
        if self.head==None:
            self.head=None
            self.tail=None
        else:
            t=self.head
            while t.next is not self.tail:
                t=t.next
            self.tail=t
            self.tail.next=None

    def popfront(self):
        if self.head==None:
            self.
    def display(self):
        t=self.head
        while t is not self.tail:
            print("["+str(t.data)+"]",end="->")
            t=t.next
        print("["+str(t.data)+"]")

while True:
    ch=int(input(" ___________________\n|choose Menu :      |\n|1.create Linkedlist|\n|2.pushback         |\n|3.pushfront        |\n|4.display          |\n|5.popback          |\n|6.popfront         |\n|___________________|  \n: "))
    if ch==1:
        s=SLL()
    elif ch==2:
        s.pushback(int(input("enter the element: ")))
    elif ch==3:
        s.pushfront(int(input("enter the element: ")))
    elif ch==4:
        s.display()
    elif ch==5:
        s.popback()
    elif ch==6:
        s.popfront()

