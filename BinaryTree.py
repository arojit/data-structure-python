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

    def inorder_traversal(self):
        current = self.root
        if current is None:
            return
        else:
            stack = []
            while current is not None or len(stack) > 0:
                while current is not None:
                    stack.append(current)
                    current = current.left

                current = stack.pop()
                print(current.data, end=", ")
                current = current.right
            print("")

    def preorder_traversal(self):
        current = self.root
        if current is None:
            return
        else:
            stack = [current]
            while len(stack) > 0:
                current = stack.pop()
                print(current.data, end=", ")

                if current.right is not None:
                    stack.append(current.right)
                if current.left is not None:
                    stack.append(current.left)
            print("")

    def postorder_traversal(self):
        current = self.root
        if current is None:
            return
        else:
            stack1 = [current]
            stack2 = []
            while len(stack1) > 0:
                current = stack1.pop()
                stack2.append(current)

                if current.left is not None:
                    stack1.append(current.left)
                if current.right is not None:
                    stack1.append(current.right)

            while len(stack2) > 0:
                current = stack2.pop()
                print(current.data, end=", ")
        print("")
    
    def level_order_traversal(self):
        current = self.root
        queue = [current]
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.data, end=", ")

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print("")


if __name__ == '__main__':
    binaryTree = BinaryTree()

    binaryTree.add(20)
    binaryTree.add(15)
    binaryTree.add(30)
    binaryTree.add(10)
    binaryTree.add(17)
    binaryTree.add(25)
    binaryTree.add(40)

    binaryTree.inorder_traversal()
    binaryTree.preorder_traversal()
    binaryTree.postorder_traversal()
    binaryTree.level_order_traversal()
