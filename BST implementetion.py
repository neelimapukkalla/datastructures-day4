#implementation of binary search tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)

node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7

print("Root Node is:")
print(node1.data)
print("left Child of the node is:")
print(node1.leftChild.data)
print("right Child of the node is:")
print(node1.rightChild.data)
print(" Node is:")
print(node2.data)
print("left child of the node is:")
print(node2.leftChild.data)
print("right child of the node is:")
print(node2.rightChild.data)
print(" Node is:")
print(node3.data)
print("left child of the node is:")
print(node3.leftChild.data)
print("right child of the node is:")
print(node3.rightChild.data)


