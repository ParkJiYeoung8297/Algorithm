import sys

n=int(sys.stdin.readline())

class Queue():
    def __init__(self):
        self.size=0
        self.q=[]
    
    def Push(self,data):
        self.q.append(data)
        self.size=self.size+1
    
    def Pop(self):
        if self.size>0:
            print(self.q[0])
            del self.q[0]
            self.size=self.size-1
        elif self.size==0:
            print(-1)
        
    def Size(self):
        print(self.size)
    
    def Empty(self):
        if self.size==0:
            print(1)
        elif self.size>0:
            print(0)
    
    def Front(self):
        if self.size>0:
            print(self.q[0])
        elif self.size==0:
            print(-1)
    
    def Back(self):
        if self.size>0:
            print(self.q[-1])
        elif self.size==0:
            print(-1)
queue=Queue()

for i in range(n):
    run=sys.stdin.readline().split()
    if run[0]=="push":
        queue.Push(run[1])
    elif run[0]=="pop":
        queue.Pop()
    elif run[0]=="size":
        queue.Size()
    elif run[0]=="empty":
        queue.Empty()
    elif run[0]=="front":
        queue.Front()
    elif run[0]=="back":
        queue.Back()
