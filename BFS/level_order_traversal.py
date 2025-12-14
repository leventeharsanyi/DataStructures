from collections import deque
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root: Node) -> list[list[int]]:
    res = []
    queue = deque([root])
    while queue:
        n = len(queue)
        level = []
        for _ in range(n):
            node = queue.popleft()
            level.append(node.value)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
    return res

if __name__ == "__main__":
    print(level_order(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))))
