class Queue:
    def __init__(self, size):
        self.size = size - 1
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.rear < self.size:
            self.rear += 1
            self.queue[self.rear] = data
            self.display()
        else:
            print("Queue is Full")

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            for i in range(self.rear):
                self.queue[i] = self.queue[i + 1]
            self.queue[self.rear] = None
            self.rear -= 1
            self.display()

    def display(self):
        for i in self.queue:
            print(i)
        print("-----------")


if __name__ == '__main__':
    queue = Queue(3)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    queue.enqueue(3)
    queue.enqueue(4)
