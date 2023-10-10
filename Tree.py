from Node import Node

class Tree(object):
    def __init__(self):
        self.getRoot = None
        self.getInOrder = []
        self.getPostOrder = []
        self.getPreOrder = []

    def createBinaryTreeByList(self,valueList):
        if(valueList[0] is not None):
            self.getRoot = Node(value=valueList[0])
            self.getTotalNodes = len(valueList)
            valueList.pop(0)
            totalValuesWIthoutRoot = len(valueList)
            valueAdded = 0

            for value in valueList:
                nodePointer = self.getRoot
                while(nodePointer is not None):
                    if(valueAdded == totalValuesWIthoutRoot):
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
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.getInOrder.append(root.value)
            self.inorder(root.right)
        
    
    def preorder(self,root):
        if root:
            self.getPreOrder.append(root.value)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self,root):   
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.getPostOrder.append(root.value)
 
 