class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"<Node: {self.data}>"

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def add(self, node: Node):
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def prepend(self, node: Node):
        node.next = self.head
        self.head = node

    def insert(self, node: Node, index: int):
        size = self.size()
        if index == 0:
            self.prepend(node)
        elif index == size:
            self.add(node)
        elif index > size:
            pass
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node

    def delete(self, node: Node):
        if self.head == node:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.data == node.data:
                curr.next = curr.next.next
                return
            curr = curr.next

    def print_list(self):
        curr = self.head
        values = []
        while curr:
            values.append(curr.data)
            curr = curr.next
        print(values)

if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.add(Node(0))
    sll.add(Node(1))
    sll.add(Node(2))
    sll.add(Node(3))
    sll.add(Node(4))
    sll.print_list()
    sll.delete(Node(3))
    sll.prepend(Node(-1))
    sll.insert(Node(5), 1)
    sll.print_list()
    print(sll.size())
    print(Node(5))
