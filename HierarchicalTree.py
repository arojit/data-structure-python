class Node:
    name = ''
    subordinates = []


class Tree:
    root = None

    def add(self, manager, subordinate):
        child_node = Node()
        child_node.name = subordinate
        child_node.subordinates = []
        if self.root is None:
            node = Node()
            node.name = manager
            node.subordinates.append(child_node)
            self.root = node
        else:
            current = self.root
            stack = [current]
            while len(stack) > 0:
                current = stack.pop()
                if current.name == manager:
                    current.subordinates.append(child_node)
                else:
                    for child in current.subordinates:
                        stack.append(child)

    def display(self):
        current = self.root
        if current is None:
            return
        else:
            queue = [current]
            while len(queue) > 0:
                current = queue[0]
                queue.remove(current)
                if len(current.subordinates) > 0:
                    print(current.name, end=' -> ')
                    for child in current.subordinates:
                        print(child.name, end=", ")
                        queue.append(child)
                    print()


if __name__ == '__main__':
    tree = Tree()

    tree.add('Bimala', 'Habal')
    tree.add('Bimala', 'Lab')
    tree.add('Bimala', 'Kush')

    tree.add('Habal', 'Arojit')
    tree.add('Habal', 'Arpita')

    tree.add('Lab', 'Madhab')
    tree.add('Lab', 'Jadav')
    tree.add('Lab', 'Parvati')

    tree.add('Kush', 'Hiren')
    tree.add('Kush', 'Milan')
    tree.add('Kush', 'Mou')

    tree.add('Arpita', 'Adrij')

    tree.display()
