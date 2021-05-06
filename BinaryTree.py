class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                parent = current
                if data < current.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return
                    

if __name__ == '__main__':
    binaryTree = BinaryTree()

    binaryTree.add(20)
    binaryTree.add(15)
    binaryTree.add(30)
    binaryTree.add(10)
    binaryTree.add(17)
    binaryTree.add(25)
    binaryTree.add(40)
