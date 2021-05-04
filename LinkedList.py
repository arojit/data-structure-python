class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.add(3)
    ll.add(5)
    ll.add(7)

    ll.show()
