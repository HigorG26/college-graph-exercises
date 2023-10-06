from Node import Node

class Tree(object):
    def __init__(self):
        self.getRoot = None

    def createBinaryTreeByList(self,valueList):
        if(valueList[0] is not None):
            self.getRoot = Node(value=valueList[0])
            valueList.pop(0)
            totalValues = len(valueList)
            valueAdded = 0

            for value in valueList:
                nodePointer = self.getRoot
                while(nodePointer is not None):
                    if(valueAdded == totalValues):
                        nodePointer = None

                    if(value < nodePointer.value):
                        if(nodePointer.left is not None):
                            nodePointer = nodePointer.left
                        else:
                            nodePointer.left = Node(value=value)
                            nodePointer = None
                    else:
                        if(nodePointer.right is not None):
                            nodePointer = nodePointer.right
                        else:
                            nodePointer.right = Node(value=value)
                            nodePointer = None

                    valueAdded+=valueAdded        
        else:
            return
        
    def inorder(root):
        if root:
            inorder(root.left)
            print(root.value, end=" ")
            inorder(root.right)
    
    def preorder(root):
        if root:
            print(root.val, end=" "),
            preorder(root.left)
            preorder(root.right)
 
    
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.val, end=" "),
 
 