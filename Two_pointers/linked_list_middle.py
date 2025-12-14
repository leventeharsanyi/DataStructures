class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

def middle(head: Node) -> Node:
    slow, fast = head, head
    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
    return slow.value

if __name__ == "__main__":
    print(middle(Node(1, Node(2, Node(3, Node(4, Node(5)))))))