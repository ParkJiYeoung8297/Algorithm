# 해설 보고 품
import sys
sys.setrecursionlimit(10**7)
class Node:
    def __init__(self,x,y,idx):
        self.x=x
        self.y=y
        self.idx=idx
        self.left=None
        self.right=None

def solution(nodeinfo):
    answer = [[],[]]
    preorder_list=[]
    postorder_list=[]
    
    info=sorted([[pos[0],pos[1],idx+1] for idx,pos in enumerate(nodeinfo)],key=lambda x: (-x[1],x[0]))

    root=Node(*info[0])
    
    # 이진 트리 만들기
    def insert(parent,child):
        if child.x < parent.x:
            if parent.left==None:
                parent.left=child
            else:
                insert(parent.left,child)
        else: 
            if parent.right==None:
                parent.right=child
            else:
                insert(parent.right,child)
                
      
    for x,y,idx in info[1:]:
        insert(root, Node(x,y,idx))
    
    
    # 전위 순회
    def preorder(node):
        if node:
            preorder_list.append(node.idx)
            preorder(node.left)
            preorder(node.right)
    
    # 후위 순회
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            postorder_list.append(node.idx)
        
    preorder(root)
    postorder(root)
    
    answer[0]=preorder_list
    answer[1]=postorder_list
    
    return answer