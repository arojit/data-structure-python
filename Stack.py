class Stack:
    def __init__(self, size):
        self.size = size - 1
        self.stack = [None for i in range(size)]
        self.tos = -1

    def push(self, data):
        if self.tos < self.size:
            self.tos += 1
            self.stack[self.tos] = data
            self.display()
        else:
            print("Stack is Full")

    def pop(self):
        if self.tos < 0:
            print("Stack is Empty")
        else:
            self.stack[self.tos] = None
            self.tos -= 1
            self.display()

    def display(self):
        for i in self.stack:
            print(i)
        print("------------")


if __name__ == '__main__':
    stack = Stack(3)

    stack.pop()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.pop()
    stack.push(4)
    stack.push(5)
    stack.pop()
    stack.pop()
    stack.pop()
