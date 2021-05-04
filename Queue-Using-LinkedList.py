class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def show(self):
        if self.head is None:
            print("Queue is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next


if __name__ == '__main__':
    queue = Queue()

    queue.show()

    queue.insert(1)
    queue.insert(4)
    queue.insert(8)

    queue.delete()
    queue.delete()
    queue.delete()
    queue.delete()

    queue.show()

