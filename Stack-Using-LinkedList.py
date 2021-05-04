class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def pop(self):
        if self.head is None:
            print("Empty Stack")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            # del current
            current.next = None

    def show(self):
        current = self.head
        if current is None:
            print("Stack empty")
        else:
            while current is not None:
                print(current.data)
                current = current.next


if __name__ == '__main__':
    stack = Stack()

    stack.show()
    print("----------")

    stack.push(3)
    stack.push(5)
    stack.push(7)

    stack.show()
    print("----------")

    stack.pop()
    stack.pop()
    stack.pop()

    stack.show()
    print("----------")

    stack.push(100)
    stack.show()
    print("----------")