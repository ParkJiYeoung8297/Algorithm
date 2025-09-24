import sys

n = int(sys.stdin.readline())
a=[]
a.append(n)
for i in range(n):
    r_data = sys.stdin.readline()
    a.append(int(r_data))

for i in range(len(a)):
    a[i]=int(a[i])

class Stack():
    def __init__(self):
        self.size=0
        self.stacklist=[]
    
    def Push(self,data):
        self.stacklist.append(data)
        self.size=self.size+1
        
    def Pop(self):
        if self.size>0:
            top=self.stacklist[-1]
            del self.stacklist[-1]
            self.size=self.size-1
            return top
        else:
            print("empty stack")
        
    def Size(self):
            return self.size
    
    def Top(self):
        if self.size>0:
            return self.stacklist[-1]
        else:
            return -1
            
b=[]
stack=Stack()
s_list=Stack()

for i in range(a[0]):
    s_list.Push(a[0]-i)

stack.Push(s_list.Pop())
b.append("+")

while(stack.size>=0):
    if b[0]=="NO":
        break
    for i in range(1,len(a)):
        while(1):
            if a[i]>stack.Top():
                stack.Push(s_list.Pop())
                b.append("+")
            elif a[i]==stack.Top():
                stack.Pop()
                b.append("-")
                break
            else:
                b=["NO"]
                break
        if b[0]=="NO":
            break
    break     
            
for i in range(len(b)):
    print(b[i])
