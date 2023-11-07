import sys

class Stack():
    def __init__(self):
        self.size=0
        self.s=[]
    def Push(self,data):
        self.s.append(data)
        self.size=self.size+1
    def Pop(self):
        data=self.s[-1]
        del self.s[-1]
        self.size=self.size-1
        return data
        
stack_front=Stack()
stack_back=Stack()

stack_front.s=list(sys.stdin.readline().rstrip())
stack_front.size=len(stack_front.s)

n=int(sys.stdin.readline())

for i in range(n):
    run=sys.stdin.readline().split()
    
    if run[0]=="L":
        if stack_front.size==0:
            pass
        elif stack_front.size>0:
            stack_back.Push(stack_front.Pop())
        else:
            print("wrong")
    elif run[0]=="D":
        if stack_back.size==0:
            pass
        elif stack_back.size>0:
            stack_front.Push(stack_back.Pop())
        else:
            print("wrong")
    elif run[0]=="B":
        if stack_front.size==0:
            pass
        elif stack_front.size>0:
            stack_front.Pop()
        else:
            print("wrong")
    elif run[0]=="P":
            stack_front.Push(run[1])
    else:
        print("wrong")

for i in range(stack_front.size):
    print(stack_front.s[i],end="")

for i in range(stack_back.size):
    print(stack_back.s[-i-1],end="")