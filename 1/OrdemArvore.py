from Tree import Tree

list = [5,2,4,12]

binaryTree = Tree()
binaryTree.createBinaryTreeByList(valueList=list)
# print(binaryTree.getRoot.value)
binaryTree.inorder(root=binaryTree.getRoot)
print(f"em-ordem: {binaryTree.getInOrder}")
binaryTree.preorder(root=binaryTree.getRoot)
print(f"pré-ordem: {binaryTree.getPreOrder}")
binaryTree.postorder(root=binaryTree.getRoot)
print(f"pós-ordem: {binaryTree.getPostOrder}")