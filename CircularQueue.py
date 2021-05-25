class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue = [None for i in range(k)]
        self.front = self.rear = -1

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if (self.rear + 1) % self.size == self.front:
            return False
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True



    def deQueue(self):
        """
        :rtype: bool
        """
        if self.front == -1:
            return False
        elif self.rear == self.front:
            # self.queue[self.front] = None
            self.rear = self.front = -1
            return True
        else:
            # self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.front == -1:
            return -1
        return self.queue[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        if self.front == -1:
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.front == -1:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if (self.rear + 1) % self.size == self.front:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
print(param_1)
param_1 = obj.enQueue(1)
print(param_1)
param_1 = obj.enQueue(1)
print(param_1)
param_1 = obj.enQueue(1)
print(param_1)
param_1 = obj.enQueue(1)
print(param_1)
param_2 = obj.deQueue()
print(param_2)
param_3 = obj.Front()
print(param_3)
param_4 = obj.Rear()
print(param_4)
param_5 = obj.isEmpty()
print(param_5)
param_6 = obj.isFull()
print(param_6)
