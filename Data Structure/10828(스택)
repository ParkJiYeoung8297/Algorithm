import sys

class Node:   #저장하려는 정보들의 묶음(세트)
    def __init__(self, data):
        self.prev = None
        self.data = int(data)

class Stack:  #linked list로 한 stack임
    def __init__(self):
        self.top = -1 # stack의 head를 가리키는 참조 변수임
        self.size = 0

    def Push(self, data):
        node = Node(data) #aggregation 관계 (Node클래스를 객체로 받음 has-a)
        if self.size == 0:  #stack이 빈공간이면 참조변수 top은 새로 들어온 node를 가리킴
            self.top = node
        else:  #stack이 빈공간이 아니면 기존top참조 변수는 새 node가 들어오기전 head인 노드를 가리키고 있을거임
            node.prev = self.top
            self.top = node
        self.size += 1

    def Pop(self):
        if self.size == 0:
            return -1
        else:
            value = self.top
            node = self.top.prev
            self.top = node
            self.size -= 1
            return value

    def Size(self):
        return self.size

    def Empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def Top(self):
        if self.size == 0:
            return -1
        else:
            return self.top


n = int(input())
stack = Stack()
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        stack.Push(a[1])
    elif a[0] == "pop":
        i = stack.Pop()
        if i == -1:
            print(i)
        else:
            print(i.data)
    elif a[0] == "size":
        print(stack.Size())
    elif a[0] == "empty":
        print(stack.Empty())
    elif a[0] == "top":
        i = stack.Top()
        if i == -1:
            print(i)
        else:
            print(i.data)
    else:
        print("Wrong!")
        

