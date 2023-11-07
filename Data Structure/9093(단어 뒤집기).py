class Node:
    def __init__(self,data):
        self.data=data.split()

class Stack:
    def __init__(self):
        self.stringlist=[]
        self.size=0;

    def push(self,data):
        node=Node(data)
        for i in range(len(node.data)):
            a=list(node.data[i])
            for j in range(len(a)):
                self.stringlist.append(a[-j-1])
                self.size+=self.size
            self.stringlist.append(" ")
            self.size+=self.size
      
n=int(input())
for i in range(n):
    a=input()
    stack=Stack()
    stack.push(a)
    for j in range(len(stack.stringlist)):
        print(stack.stringlist[j],end="")
    

        
    
