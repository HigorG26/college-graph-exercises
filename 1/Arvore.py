from No import No

class Arvore(object):
    def __init__(self):
        self.getRoot = None

    def createBinaryTreeByList(self,valueList):
        if(valueList[0] is not None):
            self.getRoot = No(value=valueList[0])
            nodePointer = self.getRoot

            for value in valueList:
                while(nodePointer is not None):
                        if(value < nodePointer.value):
                            if(nodePointer.left is not None):
                                nodePointer = nodePointer.left
                            else:
                                nodePointer.left = No(value=value)
                                nodePointer = None
                        else:
                            if(nodePointer.right is not None):
                                nodePointer = nodePointer.right
                            else:
                                nodePointer.right = No(value=value)
                                nodePointer = None
        else:
            return
        
