#this is my stack implementaion in both array and linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack_using_linkedlist:
    def __init__(self,size):
        self.head=None
        self.tail=None
        self.top=-1
        self.size=size
    def isempty(self):
        return self.top==-1
    def isfull9self):
        return self.top==self.size-1
    def push(self,ele):
        if self.isfull():
            print("overflow")
        else:
            newnode=Node(ele)
            if isempty:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail=newnode
    def pop(self):
      self.top-=1
      return self.tail.data
    
    def display(self):
        if isempty
            





class stack_using_array:
    def __init__(self,size):
        self.array=[]
        self.size=size
        self.top=-1
    
    def isempty(self):
        return self.top==-1

    def isfull(self):
        return self.top==self.size-1

    def push(self,ele):         
            if self.isfull():
                print("overflow")
            else:
                self.array.append(ele)
                self.top+=1
    def pop(self):
        if self.isempty():
            print("underflow")
        else:
            self.top-=1
            return self.array[self.top+1]
    def peek(self):
        return self.array[self.top]

    def display(self):
        for i in range(self.top,-1,-1):
            print("["+str(self.array[i])+"]",end="\n")
            
            
            
            
            
            
            


#driver code
while True:
    print(" __________________ ")
    ch=int(input("|choose Menu   :   |\n|0.exit            |\n|1.createstack     |\n|2.push            |\n|3.pop             |\n|4.peek            |\n|5.display         |\n _________________ : " ))
    if ch==1:
        if int(input("enter 0 for creating stack using array\n enter 1 for creating stack uisng linkedlist : ")):
           s=stack_using_linkedlist(int(input("enter the size : ")))
        else:
            s=stack_using_array(int(input("enter the size : ")))
        print("stack is created successfully!")
    elif ch==2:
        s.push(int(input("enter the elements : ")))
        print("element pushed into stack successfully!")
    elif ch==3:
         print(s.pop())
         print("element poped out of stack successfully!")
    elif ch==4:
         print(s.peek())
    elif ch==5:
         s.display()
    elif ch==0:
         break
    


                 
