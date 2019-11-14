class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        if(self.root == None):
            return "Tree is Empty"
        else:
            return str(self.root.data)

    def addNode(self, node):
        if self.root == None:
            self.root = node
        elif self.root.data == node.data:
            print("Node already exists")
        else:
            self.addToRoot(node,self.root)

    def addToRoot(self, node, current):
        if node.data < current.data:
            if current.left == None:
                current.left = node
            else:
                self.addToRoot(node,current.left)
        elif node.data > current.data:
            if current.right == None:
                current.right = node
            else:
                self.addToRoot(node,current.right)
        else:
          print("Node already exists")

    def getPreOrderList(self):
      list = []
      return self.addPreOrderSubtree(self.root, list)

    def addPreOrderSubtree(self, node, list):
        if node != None:
            list.append(node.data)
            list = self.addPreOrderSubtree(node.left, list)
            list = self.addPreOrderSubtree(node.right, list)
        return list

    def getPostOrderList(self):
      list = []
      return self.addPostOrderSubtree(self.root, list)

    def addPostOrderSubtree(self, node, list):
        if node != None:
            list = self.addPostOrderSubtree(node.left, list)
            list = self.addPostOrderSubtree(node.right, list)
            list.append(node.data)
        return list

    def getInOrderList(self):
      list = []
      return self.addInOrderSubtree(self.root, list)

    def addInOrderSubtree(self, node, list):
        if node != None:
            list = self.addInOrderSubtree(node.left, list)
            list.append(node.data)
            list = self.addInOrderSubtree(node.right, list)
        return list

def main():
    tree = BST()

    newNode = Node(7)
    tree.addNode(newNode)
    newNode = Node(14)
    tree.addNode(newNode)
    newNode = Node(19)
    tree.addNode(newNode)
    newNode = Node(31)
    tree.addNode(newNode)
    newNode = Node(21)
    tree.addNode(newNode)
    newNode = Node(3)
    tree.addNode(newNode)
    newNode = Node(17)
    tree.addNode(newNode)
    newNode = Node(25)
    tree.addNode(newNode)

    #Adding the same element
    newNode = Node(31)
    tree.addNode(newNode)
    
    newNode = Node(9)
    tree.addNode(newNode)


    print("Preoder list: " + str(tree.getPreOrderList()))
    print("Postorder list: " + str(tree.getPostOrderList()))
    print("Inorder list: " + str(tree.getInOrderList()))


main()
