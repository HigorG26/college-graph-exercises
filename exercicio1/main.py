from Tree import Tree

print('-=-=-= Exercício 1 -=-=-=\n')
list = [4, 5, 3, 7, 8, 12, 7, 98, 76, 21, 78, 12, 98, 67, 45, 34, 100, 21, 34, 54, 65]
binaryTree = Tree()
binaryTree.createBinaryTreeByList(valueList=list)

binaryTree.inorder(root=binaryTree.getRoot)
print(f"em-ordem: {binaryTree.getInOrder}\n")

binaryTree.preorder(root=binaryTree.getRoot)
print(f"pré-ordem: {binaryTree.getPreOrder}\n")

binaryTree.postorder(root=binaryTree.getRoot)
print(f"pós-ordem: {binaryTree.getPostOrder}\n")    