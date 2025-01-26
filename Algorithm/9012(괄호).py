#stack을 이용해서 (가 나오면 push )가 나오면 pop한다
import sys

class Stack():
    def __init__(self):
        self.size=0
        self.stacklist=[]

    def Push(self,data):
        self.stacklist.append(data)
        self.size=self.size+1
    
    def Pop(self):
        if (self.size==0):
            return None
        else:
            del self.stacklist[-1]
            self.size=self.size-1
            return self.size

n=int(sys.stdin.readline())

for i in range(n):
    stack=Stack()
    vps = list(sys.stdin.readline().rstrip())
    if (vps[0]!="("):
        print("NO")
    elif(vps[-1]!=")"):
        print("NO")
    else:
        for j in range(0,len(vps)):
            if (vps[j]=="("):
                stack.Push(vps[j])
            elif (vps[j]==")"):
                if (stack.Pop()==None):
                    stack.size=-1
                    break
            else:
                print("error")

        if (stack.size==0):
            print("YES")
        else:
            print("NO")
